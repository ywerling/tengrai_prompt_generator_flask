from flask import Blueprint, render_template, request
from forms import CharacterForm
from utils import process_character_form_data

character_bp = Blueprint('character', __name__, url_prefix='/character')


@character_bp.route("/", methods=["GET", "POST"])
def character():
    form = CharacterForm()

    if request.method == "POST":
        prompt = process_character_form_data(request.form)

        # print(prompt)
        return render_template('character.html', form=form, prompt=prompt)

    # Render the template without a result if the form is not submitted
    return render_template('character.html', form=form)
