from flask import Blueprint, jsonify

# Blueprint 생성 (이름: product_bp, URL 프리픽스: /product)
product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.route('/list')
def product_list():
    return jsonify({"message": "Product List Page"})

@product_bp.route('/detail/<int:product_id>')
def product_detail(product_id):
    return jsonify({"message": f"Product Detail for ID {product_id}"})

