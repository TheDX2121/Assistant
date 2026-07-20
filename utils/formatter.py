from utils.constants import OWNER_NAME



def user_card(
    user
):

    return f"""
👤 Name:
{user.get('first_name')}

📛 Username:
@{user.get('username','None')}

🆔 User ID:
{user.get('user_id')}

🔗 Profile:
tg://user?id={user.get('user_id')}
"""



def appointment_card(
    appointment
):

    return f"""
📅 Appointment

🆔 ID:
{appointment.get('appointment_id')}

👤 User ID:
{appointment.get('user_id')}

📆 Date:
{appointment.get('date')}

🕒 Time:
{appointment.get('time')}

📌 Status:
{appointment.get('status')}
"""