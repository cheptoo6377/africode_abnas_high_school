from app.models.mealplan import MealplanModel
from flask_restful import Resource, reqparse,abort,marshal_with,fields
from app.extension import db
from dateutil.parser import parse as date_parse
# Resource for meal plans                           


mealplan_args = reqparse.RequestParser()
mealplan_args.add_argument('date', type=date_parse)
mealplan_args.add_argument('breakfast', type=str, required=True, help='Breakfast cannot be blank')
mealplan_args.add_argument('snack', type=str, required=True, help='Snack cannot be blank')
mealplan_args.add_argument('lunch', type=str, required=True, help='Lunch cannot be blank')
mealplan_args.add_argument('dinner', type=str, required=True, help='Dinner cannot be blank')
mealplan_args.add_argument('supper', type=str, required=True, help='Supper cannot be blank')
mealplan_args.add_argument('user_id', type=int, required=True, help='User ID cannot be blank')   
                                   
mealplan_fields = {
    'id': fields.Integer,
    'date': fields.DateTime,
    'breakfast': fields.String,
    'snack': fields.String,
    'lunch': fields.String,
    'dinner': fields.String,
    'supper': fields.String,
    'user_id': fields.Integer
}

class Mealplans(Resource):
    @marshal_with(mealplan_fields)
    # get all meal plans
    def get(self):
        mealplans = MealplanModel.query.all()
        if not mealplans:
            abort(404, message='Meal plans not found')
        return mealplans

    @marshal_with(mealplan_fields)
    # create a meal plan
    def post(self):
        args = mealplan_args.parse_args()
        try:
            new_mealplan = MealplanModel(
                breakfast=args['breakfast'],
                snack=args['snack'],
                lunch=args['lunch'],
                dinner=args['dinner'],
                supper=args['supper'],
                user_id=args['user_id'])
            print(new_mealplan)
            db.session.add(new_mealplan)
            db.session.commit()
            return new_mealplan, 201
        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error creating meal plan {e}')
        
class Mealplan(Resource):
    @marshal_with(mealplan_fields)
    def get(self, id):
        mealplan = MealplanModel.query.filter_by(id=id).first()
        if not mealplan:
            abort(404, message='Meal plan not found')
        return mealplan

    @marshal_with(mealplan_fields)
    def patch(self, id):
        args = mealplan_args.parse_args()
        mealplan = MealplanModel.query.filter_by(id=id).first()
        if not mealplan:
            abort(404, message='Meal plan not found')
        
        for key, value in args.items():
            if value is not None:
               setattr(mealplan, key, value)
        
        db.session.commit()
        return mealplan
    def delete(self, id):
        mealplan = MealplanModel.query.filter_by(id=id).first()
        if not mealplan:
            abort(404, message='Meal plan not found')
        
        db.session.delete(mealplan)
        db.session.commit()
        return '', 204