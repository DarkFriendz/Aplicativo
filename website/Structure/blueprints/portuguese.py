#Assets
from flask import Blueprint, request, render_template, redirect, session

#Blueprint
blueprint_pt = Blueprint('portuguese', __name__, static_folder='static', template_folder='templates')

#Home Page
@blueprint_pt.route('/home')
def home():
    return render_template('/pt/home.html')

@blueprint_pt.route('/login')
def login():
    try:
        if session['email']:
            return redirect('/')
    except:
        return render_template('/pt/login.html')