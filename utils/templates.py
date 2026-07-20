from database.templates import get_template



async def render_template(
    name: str,
    variables: dict
):

    template = await get_template(
        name
    )


    if not template:

        return None


    text = template["text"]


    for key, value in variables.items():

        text = text.replace(
            f"{{{key}}}",
            str(value)
        )


    return text