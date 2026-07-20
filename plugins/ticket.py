from pyrogram import filters

from database.tickets import create_ticket

from utils.id_generator import generate_id



def register_ticket(app):

    @app.on_message(
        filters.command("ticket")
    )
    async def ticket_handler(
        client,
        message
    ):

        ticket_id = await generate_id(
            "tickets",
            "TKT"
        )


        await create_ticket(
            {
                "ticket_id": ticket_id,
                "user_id": message.from_user.id,
                "messages": [],
                "status": "open"
            }
        )


        await message.reply_text(
            f"""
💬 Conversation Started

🎫 Ticket ID:
#{ticket_id}

Reply your message.
"""
        )