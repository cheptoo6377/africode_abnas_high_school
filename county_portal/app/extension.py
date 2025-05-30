from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security
from flask_mail import Mail


security = Security()
mail = Mail()



db = SQLAlchemy()
migrate = Migrate()