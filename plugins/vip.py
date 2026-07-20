from pyrogram import filters

from database.vip import get_vip



def register_vip(app):

    @app.on_message(
        filters.command("vip")
    )
    async def vip_status(
        client,
        message
    ):

        vip = await get_vip(
            message.from_user.id
        )


        if vip:

            text = """
💎 VIP Membership

Status:
Active
"""

        else:

            text = """
💎 VIP Membership

Status:
Not Active
"""


        await message.reply_text(
            text
        )