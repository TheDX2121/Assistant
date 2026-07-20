from motor.motor_asyncio import AsyncIOMotorClient

from config import config


client = AsyncIOMotorClient(
    config.DATABASE_URL
)

database = client[
    config.DATABASE_NAME
]


# Main database object
db = database


async def check_database():
    """
    Check MongoDB connection.
    """

    try:
        await client.admin.command(
            "ping"
        )

        return True

    except Exception:
        return False