from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from .models import User
import random
from jinja2 import Markup

# login form
class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[Email(),DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# registration form
class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[Email(),DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

    # Generate a random number
    random1 = random.randint(1,1000)
    random2 = random.randint(1001,2000)
    random3 = random.randint(2001,3000)
    random4 = random.randint(66001,67000)
    random5 = random.randint(55001,56000)
    random6 = random.randint(5001,6000)
    random7 = random.randint(6001,7000)
    random8 = random.randint(7001,8000)
    # use random number to generate random image and set its height to 70px
    r1_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random1}.svg" style="height:70px">')
    r2_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random2}.svg" style="height:70px">')
    r3_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random3}.svg" style="height:70px">')
    r4_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random4}.svg" style="height:70px">')
    r5_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random5}.svg" style="height:70px">')
    r6_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random6}.svg" style="height:70px">')
    r7_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random7}.svg" style="height:70px">')
    r8_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random8}.svg" style="height:70px">')
    
    # collect avatar choices and ensure validator is set to on
    icon = RadioField('Choose An Avatar', choices=[(random1,r1_img),(random2,r2_img),(random3,r3_img),(random4,r4_img),(random5,r5_img),(random6,r6_img),(random7,r7_img),(random8,r8_img)], validators=[DataRequired()])

    def validate_email(form, field):   
        same_email_user = User.query.filter_by(email=field.data).first()
        if same_email_user:
            raise ValidationError("Email address is already in use")

# Edit profile form
class EditProfileForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[Email(),DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

    # Generate a random icon image
    random1 = random.randint(1,1000)
    random2 = random.randint(1001,2000)
    random3 = random.randint(2001,3000)
    random4 = random.randint(66001,67000)
    random5 = random.randint(55001,56000)
    random6 = random.randint(5001,6000)
    random7 = random.randint(6001,7000)
    random8 = random.randint(7001,8000)
    
    r1_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random1}.svg" style="height:70px">')
    r2_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random2}.svg" style="height:70px">')
    r3_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random3}.svg" style="height:70px">')
    r4_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random4}.svg" style="height:70px">')
    r5_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random5}.svg" style="height:70px">')
    r6_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random6}.svg" style="height:70px">')
    r7_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random7}.svg" style="height:70px">')
    r8_img = Markup(f'<img src ="https://avatars.dicebear.com/api/micah/{random8}.svg" style="height:70px">')
    
    icon = RadioField('Choose An Avatar', choices=[(8001,"Don't Change"),(random1,r1_img),(random2,r2_img),(random3,r3_img),(random4,r4_img),(random5,r5_img),(random6,r6_img),(random7,r7_img),(random8,r8_img)], validators=[DataRequired()])

    