from flask import Blueprint, jsonify, request
from models import User, db

# Blueprint 생성
route_users_bp = Blueprint('route_users', __name__)

# 사용자 추가 (POST)
@route_users_bp.route('/add_user', methods=['POST'])
def add_user():
    new_user = User(username="sample_user", email="user@example.com")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added!", "user_id": new_user.id})

# 사용자 목록 조회 (GET)
@route_users_bp.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

# 사용자 업데이트 (PUT)
@route_users_bp.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # 요청에서 JSON 데이터를 가져옴
    data = request.get_json()

    # 사용자 ID로 해당 사용자를 찾음
    user = User.query.get_or_404(user_id)

    # 새로운 username과 email로 업데이트
    new_username = data.get('username')
    new_email = data.get('email')

    if new_username:
        user.username = new_username
    if new_email:
        user.email = new_email

    # 데이터베이스에 변경 사항 저장
    db.session.commit()

    return jsonify({"message": f"User {user_id} updated!", "new_username": user.username, "new_email": user.email})

# 사용자 삭제 (DELETE)
@route_users_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user_id} deleted!"})