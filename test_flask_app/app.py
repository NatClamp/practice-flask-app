import os

from flask import Flask, request, render_template
from blueprints.coding import coding as coding_module

app = Flask(__name__)
app.register_blueprint(coding_module, url_prefix='/coding')

@app.route('/')
def index():
    return render_template('base.html', color='red', title='Developers')
