from utils.log_channel import send_log
from utils.meeting_keyboard import meeting_buttons
from utils.helpers import get_time



async def appointment_log(
    client,
    appointment
):

    text = f"""
📅 New Meeting Request


👤 Name:
{appointment['name']}


📛 Username:
@{appointment.get('username','None')}


🆔 User ID:
{appointment['user_id']}


🔗 Profile:
tg://user?id={appointment['user_id']}


🕒 Time:
{get_time()}
"""


    await send_log(

        client,

        text,

        meeting_buttons(
            appointment["appointment_id"]
        )

    )