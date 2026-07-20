"""
Manager Bot Version Information
"""

BOT_NAME = "Manager Bot"

VERSION = "1.0.0"

BUILD = "2026.07.20"

AUTHOR = "𝚂𝚊𝚖𝚞𝚎𝚕~"

DESCRIPTION = (
    "Personal Assistant Telegram Bot "
    "with Appointment, Emergency, Ticket, "
    "VIP and Management Systems."
)


def get_version():
    return VERSION


def get_info():
    return {
        "name": BOT_NAME,
        "version": VERSION,
        "build": BUILD,
        "author": AUTHOR,
        "description": DESCRIPTION,
    }