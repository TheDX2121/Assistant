from config import config



async def send_log(
    client,
    text,
    keyboard=None
):

    if not config.LOG_CHANNEL:
        return


    await client.send_message(

        config.LOG_CHANNEL,

        text,

        reply_markup=keyboard

    )