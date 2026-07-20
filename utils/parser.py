def extract_command(
    text: str
):

    if not text:
        return None


    if text.startswith("/"):

        return text.split()[0][1:]


    return None



def get_arguments(
    text: str
):

    if not text:
        return []


    parts = text.split()

    return parts[1:]