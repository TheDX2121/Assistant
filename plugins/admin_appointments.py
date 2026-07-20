from pyrogram import filters

from database.appointments import (
    appointments
)

from utils.permissions import is_owner



def register_admin_appointments(app):

    @app.on_message(
        filters.command(
            "appointments"
        )
    )
    async def appointments_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        text = (
            "📅 Pending Appointments\n\n"
        )


        async for item in appointments.find(
            {}
        ).limit(20):

            text += (
                f"🆔 {item.get('appointment_id')}\n"
                f"👤 {item.get('user_id')}\n"
                f"🕒 {item.get('time')}\n"
                f"📌 {item.get('status')}\n\n"
            )


        await message.reply_text(
            text
        )