from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import prompt_parameters

class GenericForm(FlaskForm):
    subject = StringField("Subject")  # , validators=[DataRequired()])
    background = StringField("Background")
    style = SelectField("Style", choices=prompt_parameters.STYLE_LIST)
    art_type = SelectField("Art Type", choices=prompt_parameters.ART_TYPE_LIST)
    camera_angle = SelectField("Camera Angle", choices=prompt_parameters.CAMERA_ANGLE_LIST)
    lighting = SelectField("Lighting", choices=prompt_parameters.LIGHTING_LIST)
    color_palette = SelectField("Color Palette", choices=prompt_parameters.COLOR_PALETTE_LIST)
    color_vibe = SelectField("Color Vibe", choices=prompt_parameters.COLOR_VIBES_LIST)
    composition = SelectField("Composition", choices=prompt_parameters.COMPOSITIONS_LIST)
    special_effect = SelectField("Special Effect", choices=prompt_parameters.SPECIAL_EFFECTS_LIST)
    miscellaneous = SelectField("Miscellaneous", choices=prompt_parameters.MISCELLANEOUS_LIST)

    submit = SubmitField("Create Prompt")

class LandscapeForm(FlaskForm):
    subject = StringField("Subject")

    submit = SubmitField("Create Prompt")