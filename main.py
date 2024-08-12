from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

#creates the flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = ('52jMEfBA3347dbefePSSiheXox3E7e')
Bootstrap5(app)

#start page of the webapplication
@app.route("/")
def home():
    return render_template('index.html')

#ensures that the application keeps running
if __name__ == "__main__":
    #remove the debug=True statement before deploment
    app.run(debug=True)