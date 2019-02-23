from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

coding = Blueprint('coding', __name__, template_folder='templates')


with open('test_flask_app.json', 'r') as file:
    users = json.loads(file.read())


def get_user(username):
    return users[username]


@coding.route('/')
def index():
    all_users = [v for k,v in users.items()]
    
    return render_template('index.html', users=all_users, color='purple')


@coding.route('/<string:username>')
def user(username: str):
    user = get_user(username)

    return render_template('user.html', user=user)
