from flask_restful import Resource, marshal_with, fields, abort, reqparse
from app.models import EnrolmentModel
from app.extension import db
from dateutil.parser import parse as date_parse

enrolment_args = reqparse.RequestParser()
enrolment_args.add_argument('enrolment_date', type=date_parse)
enrolment_args.add_argument('status',type=str)
enrolment_args.add_argument('grade',type=str)


enrolment_fields = {
    'id': fields.Integer,
    'student_id': fields.Integer,
    'course_id': fields.Integer,
    'enrolment_date': fields.String,
    'status': fields.String,
    'grade': fields.String
}


class Enrolments(Resource):
    @marshal_with(enrolment_fields)
    def get(self):
        enrolments = EnrolmentModel.query.all()
        if not enrolments:
            abort(404, message='cannot find enrolment')
        return enrolments
    
    @marshal_with(enrolment_fields)
    def post(self):
        args = enrolment_args.parse_args()

        try:
            new_enrolment = EnrolmentModel(enrolment_date=args['enrolment_date'], status=args['status'], grade=args['grade'])
            db.session.add(new_enrolment)
            db.session.commit()
            return new_enrolment, 201
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"error creating a enrolment {str(e)}")
class Enrolment(Resource):
    @marshal_with(enrolment_fields)
    def get(self, id):
        enrolment = EnrolmentModel.query.filter_by(id=id).first()
        
        if not enrolment:
            abort(404, message='enrolment not found')
        return enrolment
    
    @marshal_with(enrolment_fields)
    def patch(self, id):
        args = enrolment_args.parse_args()
        enrolment = EnrolmentModel.query.filter_by(id=id).first()
        if not enrolment:
            abort(404, message='enrolment not found')
        try:
            if args['enrolment_date']:
                enrolment.enrolment_date = args['enrolment_date']
            if args['status']:
                enrolment.status = args['status']
            if args['grade']:
                enrolment.grade = args['grade']
            db.session.commit()
            return enrolment
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"error updating a enrolment {str(e)}")
    @marshal_with(enrolment_fields)
    def delete(self, id):
        enrolment = EnrolmentModel.query.filter_by(id=id).first()
        if not enrolment:
            abort(404, message='enrolment not found')
        db.session.delete(enrolment)
        db.session.commit()
        return '', 204