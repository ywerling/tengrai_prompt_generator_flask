from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import prompt_parameters
import person_parameters

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
    description = StringField("Landscape Description")

    # Dropdown menus for various landscape characteristics
    season = SelectField("Season", choices=prompt_parameters.SEASONS_LIST)
    time_of_day = SelectField("Time of Day", choices=prompt_parameters.TIME_OF_DAY_LIST)
    weather = SelectField("Weather", choices=prompt_parameters.WEATHER_LIST)
    terrain = SelectField("Terrain", choices=prompt_parameters.TERRAIN_LIST)
    mood = SelectField("Mood", choices=prompt_parameters.MOOD_LIST)

    submit = SubmitField("Create Prompt")

class CharacterForm(FlaskForm):
    description = StringField("Character Description")

    # Dropdown menus for various landscape characteristics

    submit = SubmitField("Create Prompt")