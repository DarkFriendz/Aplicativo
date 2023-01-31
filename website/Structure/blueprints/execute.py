#Assets
from flask import Blueprint, request, render_template, redirect, session

#Blueprint
blueprint_execute = Blueprint('execute', __name__, static_folder='static', template_folder='templates')

#Website Language
@blueprint_execute.route('/execute/language', methods=['POST'])
def language():
    session['language'] = str(request.form['language'])
    if request.form['language'] == 'en':
        return redirect('/en/home')
    elif request.form['language'] == 'pt':
        return redirect('/pt/home')
    elif request.form['language'] == 'es':
        return redirect('/es/home')

#Logout
@blueprint_execute.route('/execute/logout')
def logout():
    #language = session['language']
    session.clear()
    #session['language'] = language
    return redirect('/')