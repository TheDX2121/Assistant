from datetime import datetime

import pytz

from config import config



def now():

    timezone = pytz.timezone(
        config.TIMEZONE
    )


    return datetime.now(
        timezone
    )



def format_time():

    return now().strftime(
        "%d %b %Y • %I:%M %p"
    )