from pyrogram import filters

from utils.calendar import generate_slots



def register_calendar(app):

    @app.on_message(
        filters.command("calendar")
    )
    async def calendar_handler(
        client,
        message
    ):

        slots = generate_slots(
            "13:00",
            "23:00",
            30
        )


        text = (
            "🗓 Available Meeting Slots\n\n"
        )


        for slot in slots:

            text += (
                f"• {slot}\n"
            )


        await message.reply_text(
            text
        )