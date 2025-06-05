from flask_security import RegisterForm,LoginForm
from flask_security.forms import Form,Length
from wtforms import StringField,SelectField,TextAreaField,TelField,BooleanField,SelectMultipleField
from wtforms.validators import DataRequired,Optional,ValidationError
from wtforms.widgets import CheckboxInput,ListWidget

from app.models.county import County,Department
from app.models.user import Role
class ExtendedRegisterForm(RegisterForm):
    """enhanced registration form with additional fields
    """
    first_name = StringField(
        'First Name',
        validators=[DataRequired('first name required'),Length(min=2, max=50, message='first name must be between 2 and 100 characters')])

    last_name = StringField(
        'Last Name',
        validators=[DataRequired('last name required'),Length(min=2, max=50, message='last name must be between 2 and 100 characters')]
    )

    phone_number = StringField(
        'Phone Number',
        validators=[DataRequired('phone number required'),Length(min=10, max=20, message='phone number must be between 10 and 20 characters')])

    county_id = SelectField(
        'County',
        coerce=int,
        choices=[]
        )
    def _init_(self, *args, **kwargs):                                      
            super(ExtendedRegisterForm, self)._init_(*args, **kwargs)           
            # Populate county choices dynamically                                 
            self.county_id.choices = [                                            
                (county.id, county.name)                                          
                for county in County.query.filter_by(active=True).order_by(County.
  name).all()                                                                     
            ]                                                                     
            # Add default "Select County" option                                  
            self.county_id.choices.insert(0, (0, 'Select your county...'))        
                                                                                  
    def validate_phone_number(self, field):                                   
            """Custom validator for phone number format"""                        
            if field.data:                                                        
                # Remove any non-digit characters                                 
                digits_only = ''.join(filter(str.isdigit, field.data))            
                if len(digits_only) < 10:                                         
                    raise ValidationError('Phone number must contain at least 10 digits')                                                                        
                # Update field data with cleaned format                           
                field.data = digits_only                                          
                                                                                  
    def validate_county_id(self, field):                                      
            """Ensure a valid county is selected"""                               
            if field.data == 0:                                                   
                raise ValidationError('Please select your county')
class ExtendedLoginForm(LoginForm):     
                                                                  
        def _init_(self, *args, **kwargs):                                      
            super(ExtendedLoginForm, self)._init_(*args, **kwargs)              
            # Add placeholder text and styling classes                            
            self.email.render_kw = {                                              
                'placeholder': 'Enter your email address',                        
                'class': 'form-control form-control-lg'                           
            }                                                                     
            self.password.render_kw = {                                           
                'placeholder': 'Enter your password',                             
                'class': 'form-control form-control-lg'                           
            }                                                                     
                                                                                  
class UserProfileForm(Form):                                                  
        """Form for users to update their profile information"""                  
                                                                                  
        first_name = StringField(                                                 
            'First Name',                                                         
            validators=[DataRequired(), Length(min=2, max=50)]                    
        )                                                                         
                                                                                  
        last_name = StringField(                                                  
            'Last Name',                                                          
            validators=[DataRequired(), Length(min=2, max=50)]                    
        )                                                                         
                                                                                  
        phone_number = TelField(                                                  
            'Phone Number',                                                       
            validators=[Optional(), Length(min=10, max=15)]                       
        )                                                                         
                                                                                  
        def validate_phone_number(self, field):                                   
            """Custom validator for phone number format"""                        
            if field.data:                                                        
                digits_only = ''.join(filter(str.isdigit, field.data))            
                if len(digits_only) < 10:                                         
                    raise ValidationError('Phone number must contain at least 10  digits')                                                                        
                field.data = digits_only

class MultiCheckboxField(SelectMultipleField):                                
        """Custom field for multiple checkbox selection"""                        
        widget = ListWidget(prefix_label=False)                                   
        option_widget = CheckboxInput()                                           
                                                                                  
class UserEditForm(Form):                                                     
        """Form for editing user details (admin use)"""                           
                                                                                  
        first_name = StringField(                                                 
            'First Name',                                                         
            validators=[DataRequired(), Length(min=2, max=50)]                    
        )                                                                         
                                                                                  
        last_name = StringField(                                                  
            'Last Name',                                                          
            validators=[DataRequired(), Length(min=2, max=50)]                    
        )                                                                         
                                                                                  
        phone = TelField(                                                         
            'Phone Number',                                                       
            validators=[Optional(), Length(min=10, max=20)]                       
        )                                                                         
                                                                                  
        county_id = SelectField(                                                  
            'County',                                                             
            validators=[Optional()],                                              
            coerce=int,                                                           
            choices=[]                                                            
        )                                                                         
                                                                                  
        department_id = SelectField(                                              
            'Department',                                                         
            validators=[Optional()],                                              
            coerce=int,                                                           
            choices=[]                                                            
        )                                                                         
                                                                                  
        roles = MultiCheckboxField(                                               
            'Roles',                                                              
            validators=[DataRequired('Please select at least one role')],         
            coerce=int,                                                           
            choices=[]                                                            
        )                                                                         
                                                                                  
        active = BooleanField('Active Account', default=True)                     
                                                                                  
        def _init_(self, *args, **kwargs):                                      
            super(UserEditForm, self)._init_(*args, **kwargs)                   
                                                                                  
            # Populate county choices                                             
            self.county_id.choices = [(0, 'Select County...')] + [                
                (county.id, county.name)                                          
                for county in County.query.filter_by(active=True).order_by(County.
  name).all()                                                                     
            ]                                                                     
                                                                                  
            # Populate role choices                                               
            self.roles.choices = [                                                
                (role.id, role.name.replace('_', ' ').title())                    
                for role in Role.query.order_by(Role.name).all()                  
            ]                                                                     
                                                                                  
            # Department choices will be populated via JavaScript                 
                                                                                  
class DepartmentAssignmentForm(Form):                                         
        """Form for assigning users to departments"""                             
                                                                                  
        department_id = SelectField(                                              
            'Department',                                                         
            validators=[DataRequired()],                                          
            coerce=int,                                                           
            choices=[]                                                            
        )                                                                         
                                                                                  
        def _init_(self, county_id=None, *args, **kwargs):                      
            super(DepartmentAssignmentForm, self)._init_(*args, **kwargs)       
                                                                                  
            if county_id:                                                         
                self.department_id.choices = [                                    
                    (dept.id, dept.name)                                          
                    for dept in Department.query.filter_by(                       
                        county_id=county_id, active=True                          
                    ).order_by(Department.name).all()                             
                ]
