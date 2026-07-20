from pyrogram import filters

from database.tickets import add_message
from utils.permissions import is_owner


def register_owner_reply(app):

    @app.on_message(
        filters.command("reply")
    )
    async def owner_reply(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        if len(message.command) < 3:

            await message.reply_text(
                "Usage: /reply ticket_id message"
            )

            return


        ticket_id = message.command[1]

        text = message.text.split(
            " ",
            2
        )[2]


        await add_message(
            ticket_id,
            {
                "from":
                    "owner",

                "message":
                    text
            }
        )


        await message.reply_text(
            "✅ Reply sent."
        )