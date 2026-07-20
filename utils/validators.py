def valid_username(
    username
):

    if not username:
        return False


    return len(username) >= 5



def valid_message(
    message
):

    if not message:
        return False


    if len(message.strip()) < 3:
        return False


    return True



def valid_time(
    time
):

    parts = time.split(":")


    if len(parts) != 2:
        return False


    return True