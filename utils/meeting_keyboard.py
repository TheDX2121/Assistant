from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)



def meeting_buttons(
    appointment_id
):

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "✅ Accept",

                    callback_data=
                    f"accept:{appointment_id}"

                ),

                InlineKeyboardButton(

                    "❌ Reject",

                    callback_data=
                    f"reject:{appointment_id}"

                )

            ]

        ]

    )