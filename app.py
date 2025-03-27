from flask import Flask, jsonify, render_template
from models import db, Product, User, Category
import config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)

# ORM 초기화
db.init_app(app)

# Flask-Migrate 초기화
migrate = Migrate(app, db)


@app.route('/')
def index():
    # 기본 메인 페이지 렌더링
    return render_template('index.html')

@app.route('/add_category')
def add_category():
    # 새로운 Category 객체를 생성하고 DB에 추가
    new_category = Category(name="Electronics")
    db.session.add(new_category)
    db.session.commit()
    return "Category added!"

@app.route('/add_product')
def add_product():
    # 새로운 Product 객체를 생성하고 DB에 추가
    # 이미 존재하는 Category ID를 할당하여 Product에 연결
    category = Category.query.first()  # 첫 번째 카테고리 가져오기 (예시로)
    new_product = Product(name="Laptop", price=999.99, category_id=category.id)
    db.session.add(new_product)
    db.session.commit()
    return "Product added!"



@app.route('/add_user')
def add_user():
    # 새로운 User 객체를 생성하고 DB에 추가
    new_user = User(username="sample_user", email="user@example.com")
    db.session.add(new_user)
    db.session.commit()
    return "User added!"


@app.route('/get_categories')
def get_categories():
    # DB에서 모든 Category 조회
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@app.route('/get_products')
def get_products():
    # DB에서 모든 Product 조회
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/get_users')
def get_users():
    # DB에서 모든 User 조회
    users = User.query.all()
    return render_template('users.html', users=users)



if __name__ == '__main__':
    app.run(debug=True)
