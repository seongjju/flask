from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user

from forms import LoginForm, UserCreateForm
from models import User, db

view_auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@view_auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        # 이미 존재하는 사용자가 있는지 확인
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('이미 존재하는 사용자입니다.', 'danger')
            return redirect(url_for('auth.signup'))

        # 새 사용자 생성
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data
        )
        # 비밀번호 해시화
        new_user.set_password(form.password1.data)

        # 데이터베이스에 추가
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입이 완료되었습니다.', 'success')

        return redirect(url_for('auth.login'))  # 로그인 페이지로 리다이렉트

    return render_template('auth/signup.html', form=form)


@view_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash('로그인 성공!', 'success')
            return redirect(url_for('index'))  # 로그인 후 메인 페이지로 리다이렉트
        else:
            flash('아이디나 비밀번호가 잘못되었습니다.', 'danger')

    return render_template('auth/login.html', form=form)

@view_auth_bp.route('/logout')
def logout():
    logout_user()  # 로그아웃 처리
    flash('로그아웃되었습니다.', 'info')  # 로그아웃 메시지
    return redirect(url_for('index'))  # 메인 페이지로 리다이렉트