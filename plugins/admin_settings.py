from pyrogram import filters

from database.settings import (
    get_settings,
    update_settings
)

from utils.permissions import is_owner



def register_admin_settings(app):

    @app.on_message(
        filters.command("settings")
    )
    async def settings_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        data = await get_settings()


        await message.reply_text(
            f"""
⚙️ Bot Settings

🕒 Start:
{data['meeting_start']}

🕒 End:
{data['meeting_end']}

⏳ Duration:
{data['meeting_duration']} minutes

🛠 Maintenance:
{data['maintenance_mode']}
"""
        )