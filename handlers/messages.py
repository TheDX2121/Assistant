from pyrogram import filters



def register_messages(app):

    @app.on_message(
        filters.text
    )
    async def text_handler(
        client,
        message
    ):

        # Future state handlers:
        # - Emergency reply
        # - Rejection reason
        # - Ticket conversation

        pass