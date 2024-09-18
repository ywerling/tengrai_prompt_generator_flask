from flask import Blueprint, render_template, request
from forms import GenericForm
from utils import process_generic_form_data


generic_bp = Blueprint('generic', __name__, url_prefix='/generic')


@generic_bp.route("/", methods=["GET", "POST"])
def generic():
    form = GenericForm()
    # print("Generic called")

    if request.method == "POST":
        # if form.validate_on_submit():
        # Process form data to create the prompt
        prompt = process_generic_form_data(request.form)

        # print(prompt)
        return render_template('generic_refactored.html', form=form, result=prompt)

    # Render the template without a result if the form is not submitted
    return render_template('generic_refactored.html', form=form)
