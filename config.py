import os


class Config:

    API_ID = int(
        os.getenv(
            "API_ID",
            "29296297"
        )
    )


    API_HASH = os.getenv(
        "API_HASH",
        "477a9529cfd84f4088539c6ab94351fc"
    )


    BOT_TOKEN = os.getenv(
        "BOT_TOKEN",
        ""
    )


    OWNER_ID = int(
        os.getenv(
            "OWNER_ID",
            "5094080507"
        )
    )


    OWNER_NAME = "𝚂𝚊𝚖𝚞𝚎𝚕~"


    LOG_CHANNEL = int(
        os.getenv(
            "LOG_CHANNEL",
            "-1003992468621"
        )
    )


    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb+srv://Raman:RamanOp@cluster0.faapcwf.mongodb.net/"
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