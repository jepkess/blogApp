from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField,ValidationError
from wtforms import validators
from wtforms.validators import Email
# from wtforms.validators import required
from ..models import Blogs, User,Subscriber


class BlogsForm(FlaskForm):
    title = StringField('Blog Title',[validators.DataRequired(message='Field required')])
    category=SelectField('Category', choices=[('NEWS','NEWS',('Technology','Technology'))])
    Blogs=TextAreaField('Blogs')
    Submit=SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile:
    bio = TextAreaField('Tell us about you.',[validators.DataRequired(message='Field required')]) 
    submit= SubmitField('Upload')

class SubscriberForm:
    email = TextAreaField('Enter your email address',[validators.DataRequired(message='Field required')])   
    username = TextAreaField('Enter your username', [validators.DataRequired(message='Field required')]) 
    submit=SubmitField('Submit')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email=data_field.data).first():
            raise ValidationError('email already exists')


    


