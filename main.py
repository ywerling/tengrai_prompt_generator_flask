from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import prompt_parameters
import person_parameters
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define constants
ADOBE_STOCK_IMAGES_URL = "https://stock.adobe.com/"
# OUTPUT_DESTINATION = 'output.txt'
WEBSCRAPPER_SLEEP_INTERVAL = 1

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
@app.route("/adobe", methods=["GET", "POST"])
def adobe():
    search_term = ""

    if request.method == "POST":
        search_term = request.form.get("topic")

        chrome_options = webdriver.ChromeOptions()
        # to ensure browser windows stays open set the detach parameter to True
        chrome_options.add_experimental_option("detach", False)
        driver = webdriver.Chrome(chrome_options)
        driver.get(ADOBE_STOCK_IMAGES_URL)

        # allow the page to load
        time.sleep(WEBSCRAPPER_SLEEP_INTERVAL)
        search_input = driver.find_element(By.NAME, "keyword")
        # search_input.send_keys(SEARCH_TERM)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)

        # allow the page to load
        time.sleep(1)

        # images = driver.find_elements(By.CSS_SELECTOR, "#js-img-protect alt")
        # get images from the webpage
        images = driver.find_elements(By.XPATH, "//img[@alt]")

        # this part is for testing purpose only, enable these lines for troubleshooting
        # for image in images:
        #     print(f'{image.get_attribute("alt")}{image.get_attribute("name")}\n')

        return render_template('adobe.html',
                               images=images,
                               topic=search_term )

    return render_template('adobe.html',
                                images=None,
                               topic=search_term)


#go to the character prompt creator
@app.route("/character", methods=["GET", "POST"])
def character():
    gender = person_parameters.NONE_STRING
    scene = person_parameters.NONE_STRING
    race = person_parameters.NONE_STRING
    hair_color = person_parameters.NONE_STRING
    body_type = person_parameters.NONE_STRING
    skin = person_parameters.NONE_STRING
    hair_type = person_parameters.NONE_STRING
    clothing_material = person_parameters.NONE_STRING
    clothing_color = person_parameters.NONE_STRING
    clothing_type = person_parameters.NONE_STRING
    tool = person_parameters.NONE_STRING
    tool_action = person_parameters.NONE_STRING
    background = ""

    if request.method == "POST":
        generated_prompt = ""

        gender = request.form.get("gender")
        scene = request.form.get("scene")
        race = request.form.get("race")
        hair_color = request.form.get("hair_color")
        body_type = request.form.get("body_type")
        skin = request.form.get("skin")
        hair_type = request.form.get("hair_type")
        clothing_material = request.form.get("clothing_material")
        clothing_color = request.form.get("clothing_color")
        clothing_type = request.form.get("clothing_type")
        tool = request.form.get("tool")
        tool_action = request.form.get("tool_action")
        background = request.form.get("background")

        # generated_prompt = (scene + " scene, "
        #                     + gender + " "
        #                     + race + " "
        #                     + body_type + " "
        #                     + skin + " skin "
        #                     + hair_color + " "
        #                     + hair_type + " hair "
        #                     + clothing_color + " "
        #                     + clothing_material + " "
        #                     + clothing_type + " "
        #                     + person_parameters.COMMON_PROMPT_ENDING)

        if scene != prompt_parameters.NONE_STRING:
            generated_prompt += scene
            generated_prompt += " scene, "

        if gender != prompt_parameters.NONE_STRING:
            generated_prompt += gender
            generated_prompt += " "

        if race != prompt_parameters.NONE_STRING:
            generated_prompt += race
            generated_prompt += " "

        if body_type != prompt_parameters.NONE_STRING:
            generated_prompt += body_type
            generated_prompt += " , "

        if skin != prompt_parameters.NONE_STRING:
            generated_prompt += skin
            generated_prompt += " skin, "

        if hair_color != prompt_parameters.NONE_STRING:
            generated_prompt += hair_color
            generated_prompt += " "

        if hair_type != prompt_parameters.NONE_STRING:
            generated_prompt += hair_type
            generated_prompt += " hair, "

        if clothing_color != prompt_parameters.NONE_STRING:
            generated_prompt += clothing_color
            generated_prompt += " "

        if clothing_material != prompt_parameters.NONE_STRING:
            generated_prompt += clothing_material
            generated_prompt += " "

        if clothing_type != prompt_parameters.NONE_STRING:
            generated_prompt += clothing_type
            generated_prompt += ", "

        if tool_action != prompt_parameters.NONE_STRING:
            generated_prompt += tool_action
            generated_prompt += " "

        if tool != prompt_parameters.NONE_STRING:
            generated_prompt += "a "
            generated_prompt += tool
            generated_prompt += ", "

        if background != prompt_parameters.NONE_STRING:
            generated_prompt += " the background consists of "
            generated_prompt += background
            generated_prompt += " "

# add some generic elements to the prompt often used in portrait images to increase the probability of a quality image
        generated_prompt += person_parameters.COMMON_PROMPT_ENDING

        return render_template('character.html',
                               prompt=generated_prompt,
                               genders=person_parameters.GENDER_LIST,
                               scenes=person_parameters.SCENES_LIST,
                               races=person_parameters.RACES_LIST,
                               hair_colors=person_parameters.COLORS_LIST,
                               body_types=person_parameters.BODY_TYPES_LIST,
                               skins=person_parameters.SKIN_LIST,
                               hair_types=person_parameters.HAIR_TYPES_LIST,
                               clothing_materials=person_parameters.CLOTHING_MATERIAL_LIST,
                               clothing_colors=person_parameters.COLORS_LIST,
                               clothing_types=person_parameters.CLOTHING_TYPE_LIST,
                               tool_actions=person_parameters.TOOL_ACTIONS_LIST,
                               tools=person_parameters.TOOLS_LIST,
                               gender=gender,
                               scene=scene,
                               race=race,
                               hair_color=hair_color,
                               body_type=body_type,
                               skin=skin,
                               hair_type=hair_type,
                               clothing_color=clothing_color,
                               clothing_material=clothing_material,
                               clothing_type=clothing_type,
                               tool_action=tool_action,
                               tool=tool,
                               background=background)


    return render_template('character.html',
                               prompt=None,
                               genders=person_parameters.GENDER_LIST,
                               scenes=person_parameters.SCENES_LIST,
                               races=person_parameters.RACES_LIST,
                               hair_colors=person_parameters.COLORS_LIST,
                               body_types=person_parameters.BODY_TYPES_LIST,
                               skins=person_parameters.SKIN_LIST,
                               hair_types=person_parameters.HAIR_TYPES_LIST,
                               clothing_materials=person_parameters.CLOTHING_MATERIAL_LIST,
                               clothing_colors=person_parameters.COLORS_LIST,
                               clothing_types=person_parameters.CLOTHING_TYPE_LIST,
                               tool_actions=person_parameters.TOOL_ACTIONS_LIST,
                               tools=person_parameters.TOOLS_LIST,
                               gender=gender,
                               scene=scene,
                               race=race,
                               hair_color=hair_color,
                               body_type=body_type,
                               skin=skin,
                               hair_type=hair_type,
                               clothing_color=clothing_color,
                               clothing_material=clothing_material,
                               clothing_type=clothing_type,
                               tool_action=tool_action,
                               tool=tool,
                               background=background,)


#go to the landscape prompt creator
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