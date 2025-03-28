from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app import db

from forms import QuestionForm
from models import Question

board_bp = Blueprint('board', __name__)


@board_bp.route('/create/', methods=['GET', 'POST'])
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        # 폼에서 입력받은 user_id를 사용
        user_id = form.user_id.data

        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
            user_id=user_id
        )

        db.session.add(question)
        db.session.commit()
        return redirect(url_for('board.list_questions'))  # 질문 목록 페이지로 리다이렉트

    return render_template('question_form.html', form=form)  # 질문 등록 폼

# 엔드포인트 '/list'를 정의합니다.
@board_bp.route('/list')
def list_questions():
    questions = Question.query.all()

    return render_template('board_list.html', questions=questions)