from pyrogram import filters

from utils.permissions import is_owner
from utils.keyboards import admin_keyboard



def register_admin(app):

    @app.on_message(
        filters.command("admin")
    )
    async def admin_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):

            await message.reply_text(
                "❌ Access Denied"
            )

            return


        await message.reply_text(
            """
👑 Owner Admin Panel

Choose an option:
""",
            reply_markup=admin_keyboard()
        )