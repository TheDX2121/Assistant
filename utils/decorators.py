from functools import wraps

from utils.permissions import is_owner



def owner_only(func):

    @wraps(func)

    async def wrapper(
        client,
        message,
        *args,
        **kwargs
    ):

        if not is_owner(
            message.from_user.id
        ):

            await message.reply(
                "❌ Access Denied"
            )

            return


        return await func(
            client,
            message,
            *args,
            **kwargs
        )


    return wrapper