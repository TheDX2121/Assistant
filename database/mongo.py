from motor.motor_asyncio import AsyncIOMotorClient

from config import config


client = AsyncIOMotorClient(
    config.MONGO_URI
)


db = client[
    config.DATABASE_NAME
]


async def ping_database():

    await client.admin.command(
        "ping"
    )

    return True