# 🤖 Personal Assistant Telegram Bot

Official Personal Assistant Bot of:

𝚂𝚊𝚖𝚞𝚎𝚕~

## Features

✅ Appointment Booking  
✅ Emergency Requests  
✅ Owner Contact System  
✅ Ticket Conversation System  
✅ Appointment Calendar  
✅ Automatic Reminders  
✅ Accept / Reject Meetings  
✅ VIP Membership System  
✅ Payment Records  
✅ Admin Panel  
✅ Logs System  
✅ Maintenance Mode  


# Commands

## User Commands

/start
/help
/about
/contact
/appointment
/calendar
/myappointments
/profile
/emergency
/ticket
/vip
/buyvip


## Owner Commands

/admin
/appointments
/emergencies
/tickets
/broadcast
/addvip
/removevip
/settings
/logs
/stats


# Configuration

Required:

API_ID

API_HASH

BOT_TOKEN

OWNER_ID

LOG_CHANNEL

MONGO_URI


# Database

MongoDB collections:

users

appointments

emergencies

tickets

vip

payments

logs

reminders


# Running

Install:

pip install -r requirements.txt


Start:

python bot.py


# Meeting System

Default meeting time:

13:00 - 23:00

Slot duration:

30 minutes


Owner can:

Accept meetings

Reject meetings

Send rejection reason

Manage appointments


# Version

v1.0