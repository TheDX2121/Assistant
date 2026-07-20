from pyrogram import filters

from database.appointments import (
    update_appointment
)

from utils.permissions import is_owner



def register_meeting_actions(app):

    @app.on_callback_query(
        filters.regex(
            "^accept:"
        )
    )
    async def accept_meeting(
        client,
        query
    ):

        if not is_owner(
            query.from_user.id
        ):
            return


        appointment_id = query.data.split(
            ":"
        )[1]


        await update_appointment(
            appointment_id,
            {
                "status":
                    "accepted"
            }
        )


        await query.answer(
            "Accepted"
        )



    @app.on_callback_query(
        filters.regex(
            "^reject:"
        )
    )
    async def reject_meeting(
        client,
        query
    ):

        if not is_owner(
            query.from_user.id
        ):
            return


        appointment_id = query.data.split(
            ":"
        )[1]


        await update_appointment(
            appointment_id,
            {
                "status":
                    "waiting_reason"
            }
        )


        await query.message.reply_text(
            "Send rejection reason."
        )