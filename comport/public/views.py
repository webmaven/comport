# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for, abort,
                    redirect, session)
from flask.ext.login import login_user, login_required, logout_user

from comport.extensions import login_manager
from comport.user.models import User, Invite_Code
from comport.public.forms import LoginForm
from comport.user.forms import RegisterForm
from comport.utils import flash_errors
from comport.database import db

blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            if form.user.is_admin():
                redirect_url = request.args.get("next") or url_for("admin.admin_dashboard")
                return redirect(redirect_url)
            else:

                redirect_url = request.args.get("next") or url_for("department.department_dashboard", department_id=form.user.department_id)
                return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        invite_code = Invite_Code.query.filter_by(code=form.invite_code.data).first()
        invite_code.used = True
        invite_code.save()

        new_user = User.create(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        active=True,
                        department_id=invite_code.department_id)

        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
