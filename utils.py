import prompt_parameters

def process_generic_form_data(form_data):
    # Process form data from the request and return the necessary information
    subject = form_data.get("subject")
    background = form_data.get("background")
    style = form_data.get("style")

    prompt = ""

    if len(subject) >0 :
        prompt+=subject
        prompt+=", "

    if len(background) > 0:
        prompt += background
        prompt += ", "

    if style != prompt_parameters.NONE_STRING:
        prompt += style
        prompt += "."

    return prompt

    # Continue processing all necessary fields
    # Return the processed data as needed
    # return {
    #     'subject': subject,
    #     'background': background,
    #     'style': style,
    #     # Add more fields here
    # }
