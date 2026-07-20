from pyrogram import filters

from database.emergencies import create_emergency
from utils.id_generator import generate_id
from utils.notifier import notify_owner
from utils.helpers import get_time
from utils.profile_link import create_profile_link


def register_emergency_handler(app):

    @app.on_message(
        filters.command("emergency")
    )
    async def emergency_start(
        client,
        message
    ):

        await message.reply_text(
            """
🚨 Emergency Request

Send me your message.
I will forward it to the owner.
"""
        )


    @app.on_message(
        filters.text
    )
    async def emergency_message(
        client,
        message
    ):

        # Later connected with user state system

        emergency_id = await generate_id(
            "emergencies",
            "EMG"
        )


        data = {

            "emergency_id":
                emergency_id,

            "user_id":
                message.from_user.id,

            "name":
                message.from_user.first_name,

            "username":
                message.from_user.username,

            "profile":
                create_profile_link(
                    message.from_user.id
                ),

            "message":
                message.text,

            "time":
                get_time(),

            "status":
                "pending"
        }


        await create_emergency(
            data
        )


        await notify_owner(
            client,

            f"""
🚨 Emergency Request

👤 Name:
{data['name']}

📛 Username:
@{data['username']}

🆔 User ID:
{data['user_id']}

🔗 Profile:
{data['profile']}


📝 Message:
{data['message']}

🕒 Time:
{data['time']}
"""
        )