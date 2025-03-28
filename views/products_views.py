from flask import Blueprint, render_template
from models import Product

# Blueprint 생성
view_products_bp = Blueprint('view_products', __name__)

# /get_products 라우트
@view_products_bp.route('/views_get_products')
def get_products():
    # DB에서 모든 Product 조회
    products = Product.query.all()
    # products 데이터를 products.html 템플릿에 전달
    return render_template('products.html', products=products)