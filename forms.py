from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,IntegerField
from blog.models import User
from wtforms.validators import DataRequired,ValidationError,EqualTo,Regexp,Length,Email,NumberRange
from wtforms.widgets import RangeInput,CheckboxInput


class RegistrationForm(FlaskForm):
    username= StringField(label='First name',validators=[DataRequired(),
                            Regexp('([a-z0-9]{4,20})\w+$',message='Username must be lowercase a-z and between 4-20 characters')],
                            render_kw={'placeholder':'Username'})


    email = EmailField('Email',
                        validators=[DataRequired(),Email()],
                        render_kw={'placeholder':'Email'})


    password= PasswordField('New Password',
                        validators=[DataRequired(),
                                    EqualTo('confirm', message='Passwords must be match'),
                                    Regexp('([A-Za-z0-9]{4,20})\w+$',message='Password must be between 4-20 characters and contains alphanumeric values only')],

                        render_kw={'placeholder':'Password'})
    confirm= PasswordField('Repeat Password',
                            validators=[DataRequired()],
                            render_kw={'placeholder':'Re-enter password'}) 

    submit = SubmitField('Register')

    
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username already exist. Please choose a different one.')
        if len(username.data) > 20:
            raise ValidationError('Username should Not exceed 20 characters')
        

    def validate_email(self, email):
        if User.query.filter_by(email_address=email.data).first():
            raise ValidationError('Email already exists!')

    def validate_password(self,password):
        if len(password.data) > 20:
            raise ValidationError('Password should not exceed 20 characters')

        
class LoginForm(FlaskForm):
    email= StringField('Username',validators=[DataRequired()],render_kw={'placeholder':'Username'})
    password= PasswordField('Password',validators=[DataRequired()],render_kw={'placeholder':'Password'})
    submit = SubmitField('Log In')

    def validate_email(self, email):
        if not User.query.filter_by(email_address=email.data).first():
            raise ValidationError('Email is not exists. Please check.')
      

class PostForm(FlaskForm):
    title= StringField('Title',validators=[DataRequired()],render_kw={'placeholder':'Title'})
    content= StringField('Content',validators=[DataRequired()],render_kw={'placeholder':'Content'})
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment= StringField('Comments',validators=[DataRequired()],render_kw={'placeholder':'Comment'})
    rating = IntegerField('rating',validators=[NumberRange(min=0,max=5)],widget=RangeInput(step=1),render_kw={'class':'rating rating--nojs'})
    submit = SubmitField('Comment',render_kw={'class':"btn btn-dark"})
   