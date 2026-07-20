from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def button(
    text,
    callback_data
):

    return InlineKeyboardButton(
        text,
        callback_data=callback_data
    )



def home_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                button(
                    "📅 Book Appointment",
                    "appointment"
                )
            ],

            [
                button(
                    "🚨 Emergency",
                    "emergency"
                )
            ],

            [
                button(
                    "📂 My Appointments",
                    "my_appointments"
                )
            ],

            [
                button(
                    "💬 Contact Owner",
                    "contact_owner"
                )
            ],

            [
                button(
                    "❓ Help & FAQ",
                    "help"
                )
            ]
        ]
    )



def admin_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                button(
                    "📨 Inbox",
                    "admin_inbox"
                ),
                button(
                    "📅 Calendar",
                    "admin_calendar"
                )
            ],

            [
                button(
                    "👥 Users",
                    "admin_users"
                ),
                button(
                    "📊 Statistics",
                    "statistics"
                )
            ],

            [
                button(
                    "⚙️ Settings",
                    "settings"
                )
            ]
        ]
    )