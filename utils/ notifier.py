from config import config



async def notify_owner(
    client,
    text
):

    if not config.OWNER_ID:
        return


    await client.send_message(
        config.OWNER_ID,
        text
    )



async def notify_user(
    client,
    user_id,
    text
):

    await client.send_message(
        user_id,
        text
    )