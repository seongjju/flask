from flask import Flask, render_template
from flask_login import LoginManager, current_user

from models import db, User
import config
from flask_migrate import Migrate

from routes.categories import route_categories_bp
from routes.products import route_products_bp
from routes.users import route_users_bp
from views.auth_views import view_auth_bp
from views.board_views import view_board_bp
from views.categories_views import view_categories_bp
from views.products_views import view_products_bp
from views.users_views import view_users_bp

app = Flask(__name__)
app.config.from_object(config)

# ORM 초기화
db.init_app(app)

# Flask-Migrate 초기화
migrate = Migrate(app, db)

# LoginManager 객체 생성
login_manager = LoginManager()

# LoginManager 초기화
login_manager.init_app(app)

# 로그인 페이지가 지정되지 않으면, 로그인 페이지로 리다이렉트될 경로를 설정
login_manager.login_view = 'auth.login'

# user_loader 설정: user_id로 사용자 로드하는 함수
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 데이터베이스에서 사용자 ID로 사용자 로드

# Blueprint 등록
app.register_blueprint(route_products_bp)
app.register_blueprint(route_users_bp)
app.register_blueprint(route_categories_bp)

# 템플릿 렌더링 라우트
app.register_blueprint(view_products_bp)
app.register_blueprint(view_users_bp)
app.register_blueprint(view_categories_bp)

app.register_blueprint(view_board_bp, url_prefix='/board')
app.register_blueprint(view_auth_bp, url_prefix='/auth')

# 기본 루트 경로 추가 (index.html 렌더링)
@app.route('/')
def index():
    if current_user.is_authenticated:
        print(f"Hello, {current_user.username}!")
    else:
        print("로그인 해라")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)