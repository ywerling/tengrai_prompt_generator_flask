from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import prompt_parameters

class GenericForm(FlaskForm):
    subject = StringField("Subject")  # , validators=[DataRequired()])
    background = StringField("Background")
    style = SelectField("Style", choices=prompt_parameters.STYLE_LIST)
    art_type = SelectField("Art Type", choices=prompt_parameters.ART_TYPE_LIST)
    # Additional fields as needed...
    submit = SubmitField("Create Prompt")
