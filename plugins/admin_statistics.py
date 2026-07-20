from pyrogram import filters

from database.statistics import (
    get_statistics
)

from utils.permissions import is_owner



def register_admin_statistics(app):

    @app.on_message(
        filters.command("stats")
    )
    async def stats_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        stats = await get_statistics()


        await message.reply_text(
            f"""
📊 Bot Statistics

👥 Users:
{stats['total_users']}

📅 Appointments:
{stats['total_appointments']}

🚨 Emergencies:
{stats['total_emergencies']}

🎫 Tickets:
{stats['total_tickets']}

💎 VIP:
{stats['vip_members']}
"""
        )