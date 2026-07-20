def create_profile_link(
    user_id: int
):

    return (
        f"tg://user?id={user_id}"
    )



def create_mention(
    user_id: int,
    name: str
):

    return (
        f'<a href="tg://user?id={user_id}">'
        f'{name}'
        f'</a>'
    )