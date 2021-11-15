from flask import render_template,request,redirect,url_for, abort,flash

from app.email import mail_message
from ..models import Blogs,Role,User,Comments,Subscriber
from .. import db,photos
from . import main
from flask_login import login_required, current_user
# from ..email import mail_message
from .forms import BlogsForm,CommentForm,UpdateProfile,SubscriberForm
from ..requests import getQuotes


@main.route('/',methods=['GET'])
def index(): #view function that template (home.html)

    getquotes = getQuotes()
    message= "Welcome to Awesome Blog Website!!"
    title= 'Awesome Blog'
    return render_template('home.html',getquotes = getquotes,message=message,title=title)

@main.route('/blog/', methods = ['GET','POST'])
@login_required
def new_blog(): # blog view function that renders the blog.html template.

    form = BlogsForm()

    if form.validate_on_submit():
        category = form.category.data
       
        blog= form.Blogs.data
        title=form.title.data

        #creating an instance of a blog
        new_blog = Blogs(title=title,category= category,blog= blog,user_id=current_user.id)

        title='New Blog'

        new_blog.save_blog()

        return redirect(url_for('main.index'))
    else:

        return render_template('blogs.html',blog_form= form)




@main.route('/categories')
@login_required
def category():
    '''
    function to return the blogs byform category
    '''
    category = Blogs.get_blogs()
  
    

    title = category
    return render_template('category.html',title = title, category = category)

    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username= uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username= uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data


        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    
     

@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
   
    title = 'comments'
    return render_template('comment.html',comment = comm,title = title)

@main.route('/new_comment/<int:blogs_id>', methods = ['GET', 'POST'])
@login_required
def new_comments( blogs_id):
    
    blogs = Blogs.query.filter_by(id = blogs_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comments(comment=comment,user_id=current_user.id, blogs_id=blogs_id)
        new_comment.save_comments()

        return redirect(url_for('main.category'))
    title='New Blog'
    return render_template('new_comment.html',title=title,comment_form = form,blogs_id=blogs_id)


@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comments.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect (url_for('main.index'))


@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteBlog(id):
    blog = Blogs.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/Subscribe',methods=['GET','POST'])
def One_Blog():
    
    subscribe_form = SubscriberForm()
    
    if subscribe_form.validate_on_submit():
        email=subscribe_form.email.data
        username= subscribe_form.username.data
        subscribers = Subscriber(email = email, username = username)    
        db.session.add(subscribers)
        db.session.commit()


        mail_message("You have successfully subscribed to Awesome Blog website,Thank for joining us", "email/welcome_subs", subs.email,subs=subs)
        return redirect(url_for('main.index'))
    
    return render_template('subscriber.html',subscribe_form=subscribe_form)
