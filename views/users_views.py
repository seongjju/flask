from flask import Blueprint, render_template
from models import User

# Blueprint 생성
view_users_bp = Blueprint('view_users', __name__)

# /get_users 라우트

@view_users_bp.route('/views_get_users')
def get_users():
    # DB에서 모든 User 조회
    users = User.query.all()
    # users 데이터를 users.html 템플릿에 전달
    return render_template('users.html', users=users)