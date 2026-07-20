import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Telegram
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    # Owner
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    OWNER_NAME = os.getenv("OWNER_NAME", "𝚂𝚊𝚖𝚞𝚎𝚕~")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "manager_bot"
    )

    # Channels
    LOG_CHANNEL_ID = int(
        os.getenv("LOG_CHANNEL_ID", "0")
    )
    OFFICIAL_CHANNEL = os.getenv(
        "OFFICIAL_CHANNEL",
        ""
    )

    # General
    TIMEZONE = os.getenv(
        "TIMEZONE",
        "Asia/Kolkata"
    )

    VERSION = os.getenv(
        "BOT_VERSION",
        "1.0.0"
    )

    # Appointment
    MEETING_START_TIME = os.getenv(
        "MEETING_START_TIME",
        "13:00"
    )

    MEETING_END_TIME = os.getenv(
        "MEETING_END_TIME",
        "23:00"
    )

    MEETING_DURATION = int(
        os.getenv("MEETING_DURATION", "30")
    )

    REMINDER_INTERVAL = int(
        os.getenv("REMINDER_INTERVAL", "15")
    )

    # Modes
    MAINTENANCE_MODE = (
        os.getenv(
            "MAINTENANCE_MODE",
            "false"
        ).lower() == "true"
    )

    SANDBOX_MODE = (
        os.getenv(
            "SANDBOX_MODE",
            "false"
        ).lower() == "true"
    )


config = Config()