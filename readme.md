# Hasan Can Kaya - Konusanlar Ticket Notifier

This script sends a notification to any telegram chat/group/channel when added a new available ticket to buy.

## Requirements

* Python 3.9
* Pip 21

## Installation

* Set Telegram variables; 
    - Line 8: `telegram_bot_api_key`.
    - Line 9: `telegram_chat_id`.
* Change ticket notifier paths; 
    - Line 2: [konusanlar-ticket-notifier.sh](konusanlar-ticket-notifier.sh).
    - Line 9 and 10: [konusanlar-ticket-notifier.service](konusanlar-ticket-notifier.service).
* Change systemd service variables; 
    - Line 5: [konusanlar-ticket-notifier.service](konusanlar-ticket-notifier.service). // User
    - Line 6: [konusanlar-ticket-notifier.service](konusanlar-ticket-notifier.service). // Group
* Install and run; 
    - `$ sudo cp konusanlar-ticket-notifier.service /etc/systemd/system/konusanlar-ticket-notifier.service`
    - `$ chmod +x konusanlar-ticket-notifier.sh`
    - `$ sudo systemctl daemon-reload`
    - `$ systemctl start konusanlar-ticket-notifier.service`

---

Omer Citak - 2k22
