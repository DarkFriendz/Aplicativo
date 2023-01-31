#Assets
from flask import Flask, render_template, redirect, request, session

#Blueprints
from .blueprints.english import blueprint_en
from .blueprints.portuguese import blueprint_pt
from .blueprints.espenish import blueprint_es
from .blueprints.execute import blueprint_execute

#Class Web
class web():
    #Config Web
    def __init__(self):
        #Get Website
        self.app = Flask(__name__)

        #Secret Key Website
        self.app.secret_key = 'Secret Key'

        #Register Blueprints
        self.app.register_blueprint(blueprint_en, url_prefix="/en/")
        self.app.register_blueprint(blueprint_pt, url_prefix="/pt/")
        self.app.register_blueprint(blueprint_es, url_prefix="/es/")
        self.app.register_blueprint(blueprint_execute, url_prefix="")

    #Run Site
    def run(self):
        #Index Page
        @self.app.route('/')
        def index():
            #Verification Language
            try:
                if session['language'] == 'en':
                    return redirect('/en/home')
                elif session['language'] == 'pt':
                    return redirect('/pt/home')
                elif session['language'] == 'es':
                    return redirect('/es/home')
            except:
                return render_template('index.html')

        #Run
        self.app.run(debug=True)