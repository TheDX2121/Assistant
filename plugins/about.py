from pyrogram import filters

from config import config
from version import VERSION



def register_about(app):

    @app.on_message(
        filters.command("about")
    )
    async def about_handler(
        client,
        message
    ):

        text = f"""
🤖 Personal Assistant Bot

Owner:
{config.OWNER_NAME}

Version:
v{VERSION}

Features:

📅 Appointment Manager
🚨 Emergency System
🎫 Ticket System
💎 VIP Membership
"""

        await message.reply_text(
            text
        )