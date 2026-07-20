from datetime import datetime

from config import config


def get_time():

    return datetime.now().strftime(
        "%d %b %Y • %I:%M %p"
    )



def get_profile_link(
    user_id: int
):

    return (
        f"tg://user?id={user_id}"
    )



def format_username(
    username
):

    if username:

        return f"@{username}"

    return "Not Available"



def owner_mention():

    return config.OWNER_NAME