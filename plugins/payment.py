from pyrogram import filters

from database.payments import create_payment

from utils.id_generator import generate_id



def register_payment(app):

    @app.on_message(
        filters.command("buyvip")
    )
    async def buy_vip(
        client,
        message
    ):

        payment_id = await generate_id(
            "payments",
            "PAY"
        )


        await create_payment(
            {
                "payment_id":
                    payment_id,

                "user_id":
                    message.from_user.id,

                "status":
                    "pending"
            }
        )


        await message.reply_text(
            f"""
💎 VIP Membership

Payment ID:
{payment_id}

Payment instructions will be provided.
"""
        )