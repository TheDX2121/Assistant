from pyrogram import filters

from utils.callbackdata import (
    parse_callback
)



def register_callbacks(app):

    @app.on_callback_query()
    async def callback_handler(
        client,
        query
    ):

        action, value = parse_callback(
            query.data
        )


        if action == "help":

            await query.message.edit_text(
                """
❓ Help & FAQ

Use the menu to access bot features.
"""
            )


        elif action == "contact_owner":

            await query.message.reply_text(
                """
💬 Contact Owner

Send your message.
I will forward it.
"""
            )


        else:

            await query.answer(
                "Feature coming soon."
            )