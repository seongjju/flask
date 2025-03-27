from flask import Blueprint, jsonify, request
from models import Product, db

# Blueprint 생성
route_products_bp = Blueprint('route_products', __name__)

# 제품 추가 (POST)
@route_products_bp.route('/add_product', methods=['POST'])
def add_product():
    new_product = Product(name="sample_product", price=100.0)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added!", "product_id": new_product.id})

# 제품 목록 조회 (GET)
@route_products_bp.route('/get_products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": product.id, "name": product.name, "price": product.price} for product in products])


# 제품 업데이트 (PUT)
@route_products_bp.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # 요청에서 JSON 데이터를 가져옴
    data = request.get_json()

    # 제품 ID로 해당 제품을 찾음
    product = Product.query.get_or_404(product_id)

    # 새로운 이름과 가격으로 업데이트
    new_name = data.get('name')
    new_price = data.get('price')

    if new_name:
        product.name = new_name
    if new_price:
        product.price = new_price

    # 데이터베이스에 변경 사항 저장
    db.session.commit()

    return jsonify({"message": f"Product {product_id} updated!", "new_name": product.name, "new_price": product.price})

# 제품 삭제 (DELETE)
@route_products_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": f"Product {product_id} deleted!"})