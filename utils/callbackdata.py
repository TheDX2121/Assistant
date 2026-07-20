def create_callback(
    action,
    value=None
):

    if value:

        return (
            f"{action}:{value}"
        )

    return action



def parse_callback(
    data
):

    parts = data.split(":")


    action = parts[0]


    value = None

    if len(parts) > 1:

        value = parts[1]


    return action, value