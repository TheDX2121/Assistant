from pyrogram import filters


def register_rejection_handler(app):

    @app.on_message(
        filters.text
    )
    async def rejection_reason(
        client,
        message
    ):

        # State system will connect here

        pass