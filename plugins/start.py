from pyrogram import filters

from database.users import add_user

from utils.keyboards import home_keyboard
from utils.messages import WELCOME_MESSAGE


def register_start(app):

    @app.on_message(
        filters.command("start")
    )
    async def start_handler(
        client,
        message
    ):

        user = message.from_user


        await add_user(
            user.id,
            user.first_name,
            user.username
        )


        text = WELCOME_MESSAGE.format(
            name=user.first_name
        )


        await message.reply_text(
            text,
            reply_markup=home_keyboard()
        )