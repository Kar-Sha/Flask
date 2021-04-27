from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        user = User.query.filterby(author = form.author.data)
        
        if user is None:
            newUser = User(author = form.author.data)
            db.session.add(newUser)
        # create row in Message table with user (created/found) add to the database
        messageRow = Messages(message = form.message.data, user_id = user.query.filterby(author = form.author.data).first().id)
        db.session.add(messageRow)
        db.session.commit()
        
   
    # output all messages
    # create a list of dictionaries with the following structure
    posts = 
    [{'author':'carlos', 'message':'Yo! Where you at?!'},
    {'author':'Jerry', 'message':'Home. You?'}]
    
    dictList = Messages.query.all()
    for i in someList:
        posts = post + [
            {
                'author':' {}'.format(User.query.filter_by(id = i.user_id).first().author),
                'message':' {}'.format(i.message)
            }]

    return render_template('home.html', posts=posts, form=form)

