import logging                                                                
from flask_mail import Message                                                
from app.extension import mail                                               
                                                                                  
logger = logging.getLogger(__name__)                                          
                                                                                  
def send_email(subject, recipients, text_body, html_body=None, sender=None):  
        """Enhanced email sending with logging"""                                 
        try:                                                                      
            msg = Message(                                                        
                subject=subject,                                                  
                recipients=recipients,                                            
                body=text_body,                                                   
                html=html_body,                                                   
                sender=sender                                                     
            )                                                                     
                                                                                  
            mail.send(msg)                                                        
            logger.info(f"Email sent successfully to {recipients}: {subject}")    
            return True                                                           
                                                                                  
        except Exception as e:                                                    
            logger.error(f"Failed to send email to {recipients}: {str(e)}")       
            return False