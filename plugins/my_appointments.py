from pyrogram import filters

from database.appointments import (
    get_user_appointments
)



def register_my_appointments(app):

    @app.on_message(
        filters.command(
            "myappointments"
        )
    )
    async def my_appointments(
        client,
        message
    ):

        data = await get_user_appointments(
            message.from_user.id
        )


        if not data:

            await message.reply_text(
                "📂 No appointments found."
            )

            return


        text = "📂 Your Appointments:\n\n"


        for item in data:

            text += (
                f"🆔 {item.get('appointment_id')}\n"
                f"📅 {item.get('date')}\n"
                f"🕒 {item.get('time')}\n"
                f"📌 {item.get('status')}\n\n"
            )


        await message.reply_text(
            text
        )