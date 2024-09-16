from flask import Blueprint, render_template, request
from forms import GenericForm
from utils import process_generic_form_data
import prompt_parameters

generic_bp = Blueprint('generic', __name__, url_prefix='/generic')


@generic_bp.route("/", methods=["GET", "POST"])
def generic():
    form = GenericForm()
    if form.validate_on_submit():
        form_data = process_generic_form_data(request.form)
        # Process form data to create the prompt
        # Redirect or render the template with context as needed
        return render_template('generic_refactored.html', form=form)

    return render_template('generic_refactored.html', form=form)
