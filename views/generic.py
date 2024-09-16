from flask import Blueprint, render_template, request
from forms import GenericForm
from utils import process_generic_form_data
import prompt_parameters

generic_bp = Blueprint('generic', __name__, url_prefix='/generic')


@generic_bp.route("/", methods=["GET", "POST"])
def generic():
    form = GenericForm()
    print("Generic called")
    processed_result = ""
    if request.method == "POST":
    #     print("POST")
    # if form.validate_on_submit():
        form_data = process_generic_form_data(request.form)
        print(form_data)
        # subject = form.subject.data
        background = form.background.data
        style = form.style.data

        subject = form_data['subject']

        # Process form data to create the prompt
        # Redirect or render the template with context as needed
        # Process the form data as needed (this is an example)
        processed_result = f"Subject: {subject}, Background: {background}, Style: {style}"
        print(processed_result)
        return render_template('generic_refactored.html', form=form, result=processed_result)

    # Render the template without a result if the form is not submitted
    return render_template('generic_refactored.html', form=form)
