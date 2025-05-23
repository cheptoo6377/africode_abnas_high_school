from flask_restful import Resource, marshal_with, fields, abort, reqparse
from app.models import FeeModel
from app.extension import db
from dateutil.parser import parse as date_parse


fee_args = reqparse.RequestParser()

fee_args.add_argument('amount', type=float, required=True, help="amount is required")
fee_args.add_argument('fee_type', type=str, required=True, help="fee_type is required")
fee_args.add_argument('semester',type=str)
fee_args.add_argument('payment_date', type=date_parse)
fee_args.add_argument('status',type=str)
fee_args.add_argument('student_id', type=int, required=True, help="student_id is required")

fee_fields = {
    'id': fields.Integer,
    'student_id': fields.Integer,
    'amount': fields.Float,
    'fee_type': fields.String,
    'semester': fields.String,
    'payment_date': fields.String,
    'status': fields.String
}

class Fees(Resource):
    @marshal_with(fee_fields)
    def get(self):
        fees = FeeModel.query.all()
        if not fees:
            abort(404, message='cannot find fee')
        return fees
    
    @marshal_with(fee_fields)
    def post(self):
        args = fee_args.parse_args()

        try:
            new_fee = FeeModel(amount=args['amount'], fee_type=args['fee_type'], semester=args['semester'], payment_date=args['payment_date'], status=args['status'], student_id=args['student_id'])
            db.session.add(new_fee)
            db.session.commit()
            return new_fee, 201
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"error creating a fee {str(e)}")

class Fee(Resource):
        @marshal_with(fee_fields)
        def get(self, id):
            fee = FeeModel.query.filter_by(id=id).first()
            
            if not fee:
                abort(404, message='fee not found')
            return fee
        
        @marshal_with(fee_fields)
        def patch(self, id):
            args = fee_args.parse_args()
            fee = FeeModel.query.filter_by(id=id).first()
            if not fee:
                abort(404, message='fee not found')
            fee.amount = args['amount'] 
            fee.fee_type = args['fee_type']  
            fee.semester = args['semester']
            fee.payment_date = args['payment_date']
            fee.status = args['status']
            db.session.commit()
            return fee
        @marshal_with(fee_fields)
        def delete(self, id):
            fee = FeeModel.query.filter_by(id=id).first()
            if not fee:
                abort(404, message='fee not found')
            db.session.delete(fee)
            db.session.commit()
            return '', 204
             



