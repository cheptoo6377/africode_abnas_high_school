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

    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_TRACKABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False      # Registration confirmation        
    SECURITY_SEND_PASSWORD_RESET_EMAIL = True  # Password reset instructions      
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = True # Password change notifications
    # Email templates and customization                                           
    SECURITY_EMAIL_HTML = True                 # Send HTML emails                 
    SECURITY_EMAIL_PLAINTEXT = True           # Send plain text emails
    # Email subjects (customizable)                                               
    SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to County Services Portal"         
    SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = "Password Reset Instructions"         
    SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = "Password Changed Successfully"
    # Flask-Mail Settings (Gmail SMTP)                                        
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')             
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))                         
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']                                                                      
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true','on', '1']                                                                      
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Your Gmail address     
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Your Gmail app password
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')