from flask import render_template, redirect, request, current_app, make_response, jsonify,flash,url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm
from .strategy import mobileLogin
from app.services.sms.sms_service import sendVerifyCode

template_pre = 'default/home/auth/'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = mobileLogin(form)
        if not result:
            return redirect('/')
        flash('Invalid verify_code')
    return render_template(template_pre + 'login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home.index'))


@auth.route('/ajax/sendVerify')
@auth.route('/ajax/sendVerify/<mobile>')
def sendVerify(mobile):
    sendVerifyCode(mobile)
    return jsonify({
        'status':'200',
        'msg':'ok'
        })


