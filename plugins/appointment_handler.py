from pyrogram import filters

from database.appointments import (
    check_time_available,
    create_appointment
)

from utils.id_generator import generate_id
from utils.helpers import get_time



def register_appointment_handler(app):

    @app.on_callback_query(
        filters.regex(
            "^book:"
        )
    )
    async def book_slot(
        client,
        query
    ):

        slot = query.data.split(
            ":"
        )[1]


        available = await check_time_available(
            get_time(),
            slot
        )


        if not available:

            await query.answer(
                "❌ This slot is already booked.",
                show_alert=True
            )

            return


        appointment_id = await generate_id(
            "appointments",
            "APT"
        )


        await create_appointment(
            {

                "appointment_id":
                    appointment_id,

                "user_id":
                    query.from_user.id,

                "time":
                    slot,

                "status":
                    "pending"
            }
        )


        await query.message.edit_text(
            f"""
✅ Appointment Request Sent

🆔 ID:
{appointment_id}

🕒 Time:
{slot}

Status:
Pending approval
"""
        )