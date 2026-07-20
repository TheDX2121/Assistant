from plugins.start import register_start
from plugins.help import register_help
from plugins.about import register_about
from plugins.contact import register_contact

from plugins.appointment import register_appointment
from plugins.emergency import register_emergency

from plugins.ticket import register_ticket
from plugins.my_appointments import register_my_appointments
from plugins.calendar import register_calendar

from plugins.admin import register_admin
from plugins.admin_appointments import register_admin_appointments
from plugins.admin_emergency import register_admin_emergency
from plugins.admin_tickets import register_admin_tickets
from plugins.admin_broadcast import register_admin_broadcast

from plugins.callbacks import register_callbacks



def load_plugins(app):

    register_start(app)
    register_help(app)
    register_about(app)
    register_contact(app)

    register_appointment(app)
    register_emergency(app)

    register_ticket(app)
    register_my_appointments(app)
    register_calendar(app)

    register_admin(app)
    register_admin_appointments(app)
    register_admin_emergency(app)
    register_admin_tickets(app)
    register_admin_broadcast(app)

    register_callbacks(app)