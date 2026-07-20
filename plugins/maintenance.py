from pyrogram import filters

from database.settings import get_settings

from utils.permissions import is_owner



def register_maintenance(app):

    @app.on_message(
        filters.all
    )
    async def maintenance_check(
        client,
        message
    ):

        settings = await get_settings()


        if not settings.get(
            "maintenance_mode"
        ):
            return


        if is_owner(
            message.from_user.id
        ):
            return


        await message.reply_text(
            """
🛠 Maintenance Mode

Bot is currently unavailable.
Please try again later.
"""
        )