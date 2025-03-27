from flask import Flask, render_template
from models import db
import config
from flask_migrate import Migrate

from routes.categories import route_categories_bp
from routes.products import route_products_bp
from routes.users import route_users_bp
from views.categories_views import view_categories_bp
from views.products_views import view_products_bp
from views.users_views import view_users_bp

app = Flask(__name__)
app.config.from_object(config)

# ORM 초기화
db.init_app(app)

# Flask-Migrate 초기화
migrate = Migrate(app, db)

# Blueprint 등록
# CRUD 라우트
app.register_blueprint(route_products_bp)
app.register_blueprint(route_users_bp)
app.register_blueprint(route_categories_bp)



# 템플릿 렌더링 라우트
app.register_blueprint(view_products_bp)
app.register_blueprint(view_users_bp)
app.register_blueprint(view_categories_bp)

# 기본 루트 경로 추가 (index.html 렌더링)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)