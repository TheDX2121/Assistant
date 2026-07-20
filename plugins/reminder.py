from database.reminders import (
    create_reminder
)

from utils.id_generator import generate_id



async def add_meeting_reminder(
    user_id,
    appointment_time
):

    reminder_id = await generate_id(
        "reminders",
        "REM"
    )


    await create_reminder(
        {

            "reminder_id":
                reminder_id,

            "user_id":
                user_id,

            "message":
                f"⏰ Your meeting time is {appointment_time}",

            "status":
                "pending"
        }
    )