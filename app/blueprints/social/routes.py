from flask import render_template, current_user
from flask_login import login_required
from .import bp as social 



#  routes 
@social.route('/post', methods=['GET', 'POST'])
@login_required  
def post():  
    return render_template('post.html.j2')

@social.route('/post/my_post' , methods=['GET', 'POST'])
@login_required 
def my_post(): 
    return render_template('post.html.j2', post=current_user.posts)