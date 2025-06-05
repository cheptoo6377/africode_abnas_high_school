from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

security = Security()
mail = Mail()
csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()