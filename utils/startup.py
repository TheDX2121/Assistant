from utils.logger import get_logger
from version import get_info
from config import config


logger = get_logger()


async def startup_message():

    info = get_info()

    text = f"""
🤖 '{config.OWNER_NAME}' Assistant Started

🟢 Status: Online

📦 Version: {info['version']}

⚡ Uptime Started

#BOT_STARTED
"""

    logger.info(text)

    return text