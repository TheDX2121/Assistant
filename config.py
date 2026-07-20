import os


class Config:

    API_ID = int(
        os.getenv(
            "API_ID",
            "0"
        )
    )


    API_HASH = os.getenv(
        "API_HASH",
        ""
    )


    BOT_TOKEN = os.getenv(
        "BOT_TOKEN",
        ""
    )


    OWNER_ID = int(
        os.getenv(
            "OWNER_ID",
            "0"
        )
    )


    OWNER_NAME = "𝚂𝚊𝚖𝚞𝚎𝚕~"


    LOG_CHANNEL = int(
        os.getenv(
            "LOG_CHANNEL",
            "0"
        )
    )


    MONGO_URI = os.getenv(
        "MONGO_URI",
        ""
    )


    DATABASE_NAME = (
        "personal_assistant"
    )


    TIMEZONE = (
        "Asia/Kolkata"
    )


    MEETING_START = "13:00"

    MEETING_END = "23:00"

    MEETING_DURATION = 30


    MAINTENANCE_MODE = False



config = Config()