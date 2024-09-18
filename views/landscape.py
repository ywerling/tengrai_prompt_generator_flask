from flask import Blueprint, render_template, request
from forms import LandscapeForm
from utils import process_landscape_form_data


landscape_bp = Blueprint('landscape', __name__, url_prefix='/landscape')


@landscape_bp.route("/", methods=["GET", "POST"])
def landscape():
    form = LandscapeForm()

    if request.method == "POST":

        # Process form data to create the prompt
        prompt = process_landscape_form_data(request.form)

        # print(prompt)
        return render_template('landscape.html', form=form, prompt=prompt)

    # Render the template without a result if the form is not submitted
    return render_template('landscape.html', form=form)
