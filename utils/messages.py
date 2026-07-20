from config import config


WELCOME_MESSAGE = f"""
╭━━━━━━━━━━━━━━━━━━━━╮
        👋 Welcome {{name}}!
╰━━━━━━━━━━━━━━━━━━━━╯

I'm the official Personal Assistant of **{config.OWNER_NAME}**.

I can help you with:

📅 Book an Appointment
🚨 Send an Emergency Request
📂 View Your Appointments
💬 Contact the Owner
❓ Help & FAQ

Please choose an option below.
"""


EMERGENCY_MESSAGE = """
🚨 Emergency Request

Send me your message.

I will forward it to the owner.
"""


NO_PERMISSION = """
❌ You don't have permission to use this feature.
"""


MAINTENANCE_MESSAGE = """
🛠 Bot Maintenance Mode

The bot is currently under maintenance.

Please try again later.
"""