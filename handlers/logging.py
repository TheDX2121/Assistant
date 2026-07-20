from pyrogram import filters

from utils.logger import get_logger


logger = get_logger()



def register_logging(app):

    @app.on_message(
        filters.all
    )
    async def message_log(
        client,
        message
    ):

        if message.from_user:

            logger.info(
                f"Message from {message.from_user.id}"
            )