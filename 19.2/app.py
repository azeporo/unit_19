from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def questions():
    '''creates form for asking user input'''
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)

    
@app.route("/story")
def final_story():
    '''creates story using the user inputs'''
    text =  story.generate(request.args)
    return render_template("story.html", text=text)
