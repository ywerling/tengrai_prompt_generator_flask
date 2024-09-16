import prompt_parameters

def process_generic_form_data(form_data):
    # Process form data from the request and return the necessary information
    subject = form_data.get("subject")
    background = form_data.get("background")
    style = form_data.get("style")
    art_type = form_data.get("art_type")
    camera_angle = form_data.get("camera_angle")
    lighting = form_data.get("lighting")
    color_palette = form_data.get("color_palette")
    color_vibe = form_data.get("color_vibe")
    composition = form_data.get("composition")
    special_effect = form_data.get("special_effect")
    miscellaneous = form_data.get("miscellaneous")

    prompt = ""

    if len(subject) >0 :
        prompt+=subject
        prompt+=", "

    if len(background) > 0:
        prompt += background
        prompt += ", "

    if style != prompt_parameters.NONE_STRING:
        prompt += style
        prompt += ", "

    if art_type != prompt_parameters.NONE_STRING:
        prompt += art_type
        prompt += ", "

    if camera_angle != prompt_parameters.NONE_STRING:
        prompt += camera_angle
        prompt += ", "

    if lighting != prompt_parameters.NONE_STRING:
        prompt += lighting
        prompt += ", "

    if color_palette != prompt_parameters.NONE_STRING:
        prompt += color_palette
        prompt += ", "

    if color_vibe != prompt_parameters.NONE_STRING:
        prompt += color_vibe
        prompt += ", "

    if composition != prompt_parameters.NONE_STRING:
        prompt += composition
        prompt += ", "

    if special_effect != prompt_parameters.NONE_STRING:
        prompt += special_effect
        prompt += ", "

    if miscellaneous != prompt_parameters.NONE_STRING:
        prompt += miscellaneous
        prompt += ", "

    return prompt

    # Continue processing all necessary fields
    # Return the processed data as needed
    # return {
    #     'subject': subject,
    #     'background': background,
    #     'style': style,
    #     # Add more fields here
    # }
