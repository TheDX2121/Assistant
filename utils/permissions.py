from config import config



def is_owner(
    user_id: int
):

    return user_id == config.OWNER_ID



def can_manage(
    user_id: int
):

    return is_owner(
        user_id
    )