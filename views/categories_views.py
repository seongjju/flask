from flask import Blueprint, render_template
from models import Category

# Blueprint 생성
view_categories_bp = Blueprint('view_categories', __name__)

# /get_categories 라우트
@view_categories_bp.route('/views_get_categories')
def get_categories():
    # DB에서 모든 Category 조회
    categories = Category.query.all()
    # categories 데이터를 categories.html 템플릿에 전달
    return render_template('categories.html', categories=categories)