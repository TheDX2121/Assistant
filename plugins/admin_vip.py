from pyrogram import filters

from database.vip import (
    create_vip,
    remove_vip
)

from utils.permissions import is_owner



def register_admin_vip(app):

    @app.on_message(
        filters.command("addvip")
    )
    async def add_vip_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        if len(message.command) < 2:

            await message.reply_text(
                "Usage: /addvip user_id"
            )

            return


        user_id = int(
            message.command[1]
        )


        await create_vip(
            {
                "user_id": user_id,
                "status": "active"
            }
        )


        await message.reply_text(
            "💎 VIP Added"
        )



    @app.on_message(
        filters.command("removevip")
    )
    async def remove_vip_handler(
        client,
        message
    ):

        if not is_owner(
            message.from_user.id
        ):
            return


        user_id = int(
            message.command[1]
        )


        await remove_vip(
            user_id
        )


        await message.reply_text(
            "❌ VIP Removed"
        )