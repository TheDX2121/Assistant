from pyrogram import filters

from utils.calendar import generate_slots
from utils.keyboards import button

from pyrogram.types import InlineKeyboardMarkup



def register_appointment(app):

    @app.on_message(
        filters.command("appointment")
    )
    async def appointment_handler(
        client,
        message
    ):

        slots = generate_slots(
            "13:00",
            "23:00",
            30
        )


        buttons = []

        for slot in slots:

            buttons.append(
                [
                    button(
                        f"🕒 {slot}",
                        f"book:{slot}"
                    )
                ]
            )


        await message.reply_text(
            """
📅 Book Appointment

Choose your preferred time:
""",
            reply_markup=InlineKeyboardMarkup(
                buttons
            )
        )