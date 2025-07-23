from datetime import datetime
from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(10), index=True)
    period = db.Column(db.String(10))
    number = db.Column(db.Integer)
    category = db.Column(db.String(50))
    question_text = db.Column(db.Text)
    explanation = db.Column(db.Text)
    choices = db.relationship('Choice', backref='question', lazy='dynamic')
    answers = db.relationship('UserAnswer', backref='question', lazy='dynamic')

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_symbol = db.Column(db.String(1))
    choice_text = db.Column(db.Text)
    is_correct = db.Column(db.Boolean, default=False)

class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    selected_choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'))
    is_correct = db.Column(db.Boolean)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)
    selected_choice = db.relationship('Choice')