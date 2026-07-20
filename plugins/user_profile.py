from pyrogram import filters

from database.users import get_user

from utils.formatter import user_card


def register_profile(app):

    @app.on_message(
        filters.command("profile")
    )
    async def profile(
        client,
        message
    ):

        user = await get_user(
            message.from_user.id
        )


        if not user:

            await message.reply_text(
                "Profile not found."
            )

            return


        await message.reply_text(
            user_card(user)
        )