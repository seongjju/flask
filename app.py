from flask import Flask, jsonify
from models import db, Product, User
import config

app = Flask(__name__)
app.config.from_object(config)

# ORM 초기화
db.init_app(app)

@app.route('/add_product')
def add_product():
    # 새로운 Product 객체를 생성하고 DB에 추가
    new_product = Product(name="Sample Product", price=19.99)
    db.session.add(new_product)
    db.session.commit()
    return "Product added!"

@app.route('/get_products')
def get_products():
    # DB에서 모든 Product 조회
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])


@app.route('/add_user')
def add_user():
    # 새로운 User 객체를 생성하고 DB에 추가
    new_user = User(username="sample_user", email="user@example.com")
    db.session.add(new_user)
    db.session.commit()
    return "User added!"

@app.route('/get_users')
def get_users():
    # DB에서 모든 User 조회
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


if __name__ == '__main__':
    app.run(debug=True)
