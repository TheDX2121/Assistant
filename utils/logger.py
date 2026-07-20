import logging

from colorlog import ColoredFormatter


formatter = ColoredFormatter(
    "%(log_color)s%(levelname)s%(reset)s "
    "%(message)s"
)


handler = logging.StreamHandler()

handler.setFormatter(
    formatter
)


logger = logging.getLogger(
    "ManagerBot"
)

logger.setLevel(
    logging.INFO
)

logger.addHandler(
    handler
)


def get_logger():

    return logger