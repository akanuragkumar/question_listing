from flask_restplus import fields
from sqlalchemy import ForeignKey
from app import db
from app.v1 import v1_api


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    question = db.Column(db.String(500))
    grade = db.Column(db.Integer(), default=10)

    question_resource_model = v1_api.model('Question', {
        'id': fields.Integer(readOnly=True, description='The question unique identifier. ReadOnly.'),
        'question': fields.String(required=True, description='The question details'),
        'grade': fields.Integer(description='Grade to which question belongs')
    })
