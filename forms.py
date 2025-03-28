# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])
    user_id = IntegerField('User ID', validators=[DataRequired()])  #
