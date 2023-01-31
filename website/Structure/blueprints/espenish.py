#Assets
from flask import Blueprint, request, render_template, redirect, session

#Blueprint
blueprint_es = Blueprint('espenish', __name__, static_folder='static', template_folder='templates')

#Home Page
@blueprint_es.route('/home')
def home():
    return render_template('/es/home.html')