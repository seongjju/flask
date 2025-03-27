# from flask import Blueprint, jsonify
#
# # Blueprint 생성 (이름: user_bp, URL 프리픽스: /user)
# user_bp = Blueprint('user', __name__, url_prefix='/user')
#
# @user_bp.route('/profile')
# def profile():
#     return jsonify({"message": "User Profile Page"})
#
# @user_bp.route('/settings')
# def settings():
#     return jsonify({"message": "User Settings Page"})