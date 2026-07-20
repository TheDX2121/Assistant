from scheduler.appointment_scheduler import (
    start_scheduler
)

from scheduler.reminder_scheduler import (
    start_reminder_scheduler
)

from scheduler.cleanup_scheduler import (
    start_cleanup
)

from scheduler.vip_scheduler import (
    start_vip_scheduler
)

from scheduler.backup_scheduler import (
    start_backup_scheduler
)



def start_all_tasks(client):

    start_scheduler()

    start_reminder_scheduler(
        client
    )

    start_cleanup()

    start_vip_scheduler()

    start_backup_scheduler()