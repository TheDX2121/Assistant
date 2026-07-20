from pyrogram import filters



def register_help(app):

    @app.on_message(
        filters.command("help")
    )
    async def help_handler(
        client,
        message
    ):

        text = """
❓ Help & FAQ

Commands:

/start - Open menu
/help - Show help
/myappointments - View appointments

Features:

📅 Appointment booking
🚨 Emergency requests
💬 Contact owner
📂 Appointment history
"""

        await message.reply_text(
            text
        )