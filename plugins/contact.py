from pyrogram import filters

from utils.keyboards import button

from pyrogram.types import InlineKeyboardMarkup



def register_contact(app):

    @app.on_message(
        filters.command("contact")
    )
    async def contact_handler(
        client,
        message
    ):

        keyboard = InlineKeyboardMarkup(
            [
                [
                    button(
                        "💬 Contact Owner",
                        "contact_owner"
                    )
                ]
            ]
        )


        await message.reply_text(
            """
💬 Contact Owner

Press the button below
to send a message to the owner.
""",
            reply_markup=keyboard
        )