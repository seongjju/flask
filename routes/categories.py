from flask import Blueprint, jsonify, request
from models import Category, db

# Blueprint 생성
route_categories_bp = Blueprint('route_categories', __name__)

# 카테고리 추가 (POST)
@route_categories_bp.route('/add_category', methods=['POST'])
def add_category():
    new_category = Category(name="sample_category")
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category added!", "category_id": new_category.id})

# 카테고리 목록 조회 (GET)
@route_categories_bp.route('/get_categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{"id": category.id, "name": category.name} for category in categories])



# 카테고리 업데이트 (PUT)
@route_categories_bp.route('/update_category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    # 요청에서 JSON 데이터를 가져옴
    data = request.get_json()

    # 카테고리 ID로 해당 카테고리를 찾음
    category = Category.query.get_or_404(category_id)

    # 새로운 이름으로 업데이트
    new_name = data.get('name')
    if new_name:
        category.name = new_name

    # 데이터베이스에 변경 사항 저장
    db.session.commit()

# 카테고리 삭제 (DELETE)
@route_categories_bp.route('/delete_category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": f"Category {category_id} deleted!"})