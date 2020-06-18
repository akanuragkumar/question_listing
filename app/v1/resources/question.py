from flask_restplus import Resource, Namespace
from app import db
from app.v1 import v1_api
from .auth import token_required
from ..models.question import Question as Question_Model

question_ns = Namespace('question')


@question_ns.route('/')
class QuestionList(Resource):
    @question_ns.marshal_with(Question_Model.question_resource_model)
    @token_required
    def get(self, current_user):
        questions = Question_Model.query.filter_by(user=current_user).all()
        return questions

    @question_ns.expect(Question_Model.question_resource_model, validate=True)
    @question_ns.marshal_with(Question_Model.question_resource_model)
    @token_required
    def post(self, current_user):
        question = v1_api.payload['question']
        try:
            grade = v1_api.payload['grade']
        except KeyError:
            grade = 10

        questions = Question_Model(question=question, grade=grade, user=current_user)
        db.session.add(questions)
        db.session.commit()
        return questions


@question_ns.route('/<int:id>')
class Question(Resource):
    @question_ns.response(404, 'Question not found or you don\'t have permission to view it')
    @question_ns.marshal_with(Question_Model.question_resource_model)
    @token_required
    def get(self, id, current_user):
        questions = Question_Model.query.filter_by(user=current_user, id=id).first_or_404()
        return questions

    @question_ns.response(404, 'Question not found or you don\'t have permission to edit it')
    @question_ns.expect(Question_Model.question_resource_model, validate=True)
    @question_ns.marshal_with(Question_Model.question_resource_model)
    @token_required
    def put(self, id, current_user):
        """Get one question"""
        question = v1_api.payload['question']
        try:
            grade = v1_api.payload['grade']
        except KeyError:
            grade = 10

        questions = Question_Model.query.filter_by(user=current_user, id=id).first_or_404()

        questions.question = question
        if 'grade' in v1_api.payload:
            questions.grade = v1_api.payload['grade']

        db.session.add(questions)
        db.session.commit()

        return questions

    @question_ns.response(404, 'Question not found or you don\'t have permission to delete it')
    @question_ns.response(204, 'Question deleted')
    @token_required
    def delete(self, id, current_user):
        """Delete one question"""
        questions = Question_Model.query.filter_by(user=current_user, id=id).first_or_404()

        db.session.delete(questions)
        db.session.commit()

        return '', 204
