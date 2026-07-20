from pyrogram import filters

from utils.messages import EMERGENCY_MESSAGE


def register_emergency(app):

    @app.on_message(
        filters.command("emergency")
    )
    async def emergency_handler(
        client,
        message
    ):

        await message.reply_text(
            EMERGENCY_MESSAGE
        )