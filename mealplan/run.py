from app import app
from app.extension import db


with app.app_context():
       db.create_all()
       print("Tables created successfully")

       
if __name__ == "__main__":
    app.run(debug=True)