from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime

from flask_login import current_user

from app import db

from forms import QuestionForm
from models import Question

view_board_bp = Blueprint('board', __name__)


@view_board_bp.route('/create/', methods=['GET', 'POST'])
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        if current_user.is_authenticated:
            question = Question(
                subject=form.subject.data,
                content=form.content.data,
                create_date=datetime.now(),
                user_id=current_user.id
            )

            db.session.add(question)
            db.session.commit()
            flash('질문이 성공적으로 등록되었습니다.', 'success')  # 성공 메시지
            return redirect(url_for('board.list_questions'))  # 질문 목록 페이지로 리다이렉트
        else:
            flash('로그인 후 질문을 작성할 수 있습니다.', 'warning')  # 로그인되지 않은 경우 경고 메시지
    else:
        print(form.errors)  # 폼 검증 실패 이유 출력
    return render_template('question_form.html', form=form)  # 질문 등록 폼

@view_board_bp.route('/list')
def list_questions():
    questions = Question.query.all()

    return render_template('board_list.html', questions=questions)