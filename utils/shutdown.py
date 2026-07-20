from utils.logger import get_logger


logger = get_logger()


async def shutdown_message():

    text = """
🔴 Bot Shutdown

Status: Offline

#BOT_STOPPED
"""

    logger.warning(text)

    return text