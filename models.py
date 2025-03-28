from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))  # 역참조 설정

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}


# Question 모델 추가
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)  # 질문 제목
    content = db.Column(db.Text, nullable=False)  # 질문 내용
    create_date = db.Column(db.DateTime, nullable=False)  # 질문 등록 날짜
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 사용자 ID (FK)

    user = db.relationship('User', backref=db.backref('questions', lazy=True))  # 사용자와 질문의 관계 설정

    def to_dict(self):
        return {"id": self.id, "subject": self.subject, "content": self.content, "create_date": self.create_date,
                "user_id": self.user_id}