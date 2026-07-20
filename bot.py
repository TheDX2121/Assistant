import asyncio

from pyrogram import Client

from config import config
from version import get_info


bot = Client(
    "ManagerBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)


async def startup():
    info = get_info()

    print(
        f"""
🤖 {info['name']}

Version:
{info['version']}

Owner:
{config.OWNER_NAME}

Status:
Starting...
"""
    )


async def main():
    await startup()

    async with bot:
        print(
            "✅ Bot Started Successfully"
        )

        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())