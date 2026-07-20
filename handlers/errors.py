from utils.logger import get_logger


logger = get_logger()



def register_errors(app):

    @app.on_error()
    async def error_handler(
        client,
        error
    ):

        logger.error(
            str(error)
        )