from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import prompt_parameters

#creates the flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = ('52jMEfBA3347dbefePSSiheXox3E7e')
Bootstrap5(app)

#go to the generic template creator
@app.route("/generic", methods=["GET", "POST"])
def generic():
    subject = ""
    background = ""
    style = prompt_parameters.NONE_STRING

    print("generic called")
    if request.method == "POST":
        # Capture form data
        subject = request.form.get("subject")
        background = request.form.get("background")
        style = request.form.get("style")

        # Process the form data to create the generated prompt
        generated_prompt = f"Subject: {subject}, Background: {background}, Style: {style}"
        print(generated_prompt)

        return render_template("generic.html", prompt=generated_prompt, styles=prompt_parameters.STYLE_LIST,
                               subject=subject, background=background, style=style)

    return render_template("generic.html", prompt=None, styles=prompt_parameters.STYLE_LIST,
                           subject=subject, background=background, style=style)

#go to the generic template creator
@app.route("/landscape")
def landscape():
    return render_template('landscape.html')

#start page of the webapplication
@app.route("/")
def home():
    return render_template('index.html')

#ensures that the application keeps running
if __name__ == "__main__":
    #remove the debug=True statement before deployment
    app.run(debug=True)