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
    art_type = prompt_parameters.NONE_STRING
    camera_angle = prompt_parameters.NONE_STRING
    lighting = prompt_parameters.NONE_STRING
    color_palette = prompt_parameters.NONE_STRING
    special_effect = prompt_parameters.NONE_STRING
    color_vibe = prompt_parameters.NONE_STRING
    composition = prompt_parameters.NONE_STRING
    miscellaneous = prompt_parameters.NONE_STRING

    print("generic called")
    if request.method == "POST":
        # Capture form data
        subject = request.form.get("subject")
        background = request.form.get("background")
        style = request.form.get("style")
        art_type = request.form.get("art_type")
        camera_angle = request.form.get("camera_angle")
        lighting = request.form.get("lighting")
        color_palette = request.form.get("color_palette")
        special_effect = request.form.get("special_effect")
        color_vibe = request.form.get("color_vibe")
        composition = request.form.get("composition")
        miscellaneous = request.form.get("miscellaneous")

        # Process the form data to create the generated prompt
        # generated_prompt = f"{art_type}, {subject}, {background}, {style}, {camera_angle}, {lighting}, {color_palette}, {special_effect}, {color_vibe}, {composition}"

        generated_prompt = ""

        if art_type != prompt_parameters.NONE_STRING:
            generated_prompt += art_type
            generated_prompt += " of "

        if len(subject) > 0:
            generated_prompt += subject
            generated_prompt += " "

        if len(background) > 0:
            generated_prompt += "with "
            generated_prompt += background
            generated_prompt += " in the background "

        if style != prompt_parameters.NONE_STRING:
            generated_prompt += style
            generated_prompt += ", "

        if camera_angle != prompt_parameters.NONE_STRING:
            generated_prompt += camera_angle
            generated_prompt += ", "

        if lighting != prompt_parameters.NONE_STRING:
            generated_prompt += lighting
            generated_prompt += ", "

        if color_palette != prompt_parameters.NONE_STRING:
            generated_prompt += color_palette
            generated_prompt += ", "

        if color_vibe != prompt_parameters.NONE_STRING:
            generated_prompt += color_vibe
            generated_prompt += " color vibe, "

        if composition != prompt_parameters.NONE_STRING:
            generated_prompt += composition
            generated_prompt += " composition, "

        if special_effect != prompt_parameters.NONE_STRING:
            generated_prompt += special_effect
            generated_prompt += ", "

        if miscellaneous != prompt_parameters.NONE_STRING:
            generated_prompt += miscellaneous
            generated_prompt += ", "


        print(generated_prompt)

        return render_template("generic.html",
                               prompt=generated_prompt,
                               styles=prompt_parameters.STYLE_LIST,
                               art_types =prompt_parameters.ART_TYPE_LIST,
                               camera_angles=prompt_parameters.CAMERA_ANGLE_LIST,
                               lightings=prompt_parameters.LIGHTING_LIST,
                               color_palettes=prompt_parameters.COLOR_PALETTE_LIST,
                               special_effects=prompt_parameters.SPECIAL_EFFECTS_LIST,
                               color_vibes=prompt_parameters.COLOR_VIBES_LIST,
                               compositions=prompt_parameters.COMPOSITIONS_LIST,
                               miscellaneouss=prompt_parameters.MISCELLANEOUS_LIST,
                               subject=subject,
                               background=background,
                               style=style,
                               art_type=art_type,
                               camera_angle=camera_angle,
                               lighting=lighting,
                               color_palette=color_palette,
                               special_effect=special_effect,
                               color_vibe=color_vibe,
                               composition=composition,
                               miscellaneous=miscellaneous)

    return render_template("generic.html",
                           prompt=None,
                           styles=prompt_parameters.STYLE_LIST,
                           art_types =prompt_parameters.ART_TYPE_LIST,
                           camera_angles=prompt_parameters.CAMERA_ANGLE_LIST,
                           lightings=prompt_parameters.LIGHTING_LIST,
                           color_palettes=prompt_parameters.COLOR_PALETTE_LIST,
                           special_effects=prompt_parameters.SPECIAL_EFFECTS_LIST,
                           color_vibes=prompt_parameters.COLOR_VIBES_LIST,
                           compositions=prompt_parameters.COMPOSITIONS_LIST,
                           miscellaneouss=prompt_parameters.MISCELLANEOUS_LIST,
                           style=style,
                           art_type=art_type,
                           camera_angle=camera_angle,
                           lighting=lighting,
                           color_palette=color_palette,
                           special_effect=special_effect,
                           color_vibe=color_vibe,
                           composition=composition,
                           miscellaneous=miscellaneous)

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