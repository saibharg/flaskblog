from flask import render_template,redirect,url_for,flash
from blog import app,db
from blog.models import User, Post, Comment
from blog.forms import RegistrationForm, LoginForm, PostForm, CommentForm
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash



@app.route('/')
def header():
    data=Post.query.all()
    return render_template('home.html',data=data)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # save the content to db
        user = User(username=form.username.data,email_address=form.email.data,password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('header'))
    return render_template('register.html',form=form,title='Register')




@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email_address=form.email.data).first()
        if check_password_hash(u.password,form.password.data):
            login_user(u)
            flash('login successful')
            return redirect(url_for('header'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html',form=form,title='Login') 


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout successful')
    return redirect(url_for('header')) 

@app.route('/post',methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        p= Post(content=form.content.data,title=form.title.data,user_id=current_user.id)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('header'))
    return render_template('temp.html',form=form,title='Post')    

@app.route('/post/<id>',methods=['GET','POST'])
def post_view(id):
    view=Post.query.get_or_404(id)
    
    form = CommentForm()
    if form.validate_on_submit():
        c=Comment(comment=form.comment.data,post_id=view.id,author_id=current_user.username)        
        db.session.add(c)
        db.session.commit()  
        return redirect(url_for('post_view',id=id))

    comments = Comment.query.filter_by(post_id=id).all()

    return render_template('post.html',form=form,i=view,comments=comments)





