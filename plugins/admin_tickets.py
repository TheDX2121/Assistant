from pyrogram import filters

from database.tickets import tickets

from utils.permissions import is_owner



def register_admin_tickets(app):

    @app.on_message(
        filters.command("tickets")
    )
    async def ticket_list(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        text = (
            "🎫 Open Tickets\n\n"
        )


        async for item in tickets.find(
            {}
        ).limit(20):

            text += (
                f"🎫 {item.get('ticket_id')}\n"
                f"👤 {item.get('user_id')}\n"
                f"📌 {item.get('status')}\n\n"
            )


        await message.reply_text(
            text
        )