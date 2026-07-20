from pyrogram import filters

from utils.permissions import is_owner
from utils.broadcaster import broadcast



def register_admin_broadcast(app):

    @app.on_message(
        filters.command("broadcast")
    )
    async def broadcast_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        if len(
            message.command
        ) < 2:

            await message.reply_text(
                "Usage: /broadcast message"
            )

            return


        text = (
            message.text
            .split(
                " ",
                1
            )[1]
        )


        result = await broadcast(
            client,
            text
        )


        await message.reply_text(
            f"""
📢 Broadcast Completed

✅ Sent:
{result['success']}

❌ Failed:
{result['failed']}
"""
        )