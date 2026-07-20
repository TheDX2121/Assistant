from datetime import datetime, timedelta


def generate_slots(
    start_hour,
    end_hour,
    duration
):

    slots = []


    current = datetime.strptime(
        start_hour,
        "%H:%M"
    )

    end = datetime.strptime(
        end_hour,
        "%H:%M"
    )


    while current < end:

        slots.append(
            current.strftime(
                "%I:%M %p"
            )
        )

        current += timedelta(
            minutes=duration
        )


    return slots