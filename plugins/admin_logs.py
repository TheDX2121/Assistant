from pyrogram import filters

from database.logs import get_logs

from utils.permissions import is_owner



def register_admin_logs(app):

    @app.on_message(
        filters.command("logs")
    )
    async def logs_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        logs = await get_logs()


        text = "📜 Latest Logs\n\n"


        for log in logs:

            text += (
                f"• {log.get('message')}\n"
            )


        await message.reply_text(
            text
        )