from pyrogram import filters

from database.emergencies import emergencies

from utils.permissions import is_owner



def register_admin_emergency(app):

    @app.on_message(
        filters.command("emergencies")
    )
    async def emergency_list(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        text = (
            "🚨 Emergency Requests\n\n"
        )


        async for item in emergencies.find(
            {}
        ).limit(20):

            text += (
                f"🆔 {item.get('emergency_id')}\n"
                f"👤 {item.get('user_id')}\n"
                f"📝 {item.get('message')}\n\n"
            )


        await message.reply_text(
            text
        )