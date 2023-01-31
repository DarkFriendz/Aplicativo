#Assets
from flask import Blueprint, request, render_template, redirect, session

#Blueprint
blueprint_en = Blueprint('english', __name__, static_folder='static', template_folder='templates')

#Home Page
@blueprint_en.route('/home')
def home():
    return render_template('/en/home.html')