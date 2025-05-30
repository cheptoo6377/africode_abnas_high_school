import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///site.db") 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") 
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "default_salt")
    SECURITY_PASSWORD_HASH = os.getenv("SECURITY_PASSWORD_HASH", "bcrypt")
                                                       
            #flask security settings

    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_PASSWORD_HASH = "bcrypt"