import logging
from datetime import datetime
import notify2
from time import time, sleep
from dbus.mainloop.glib import DBusGMainLoop


PAUSE = False

date = datetime.today().strftime('%d-%m-%Y')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs/timetracker_{}.log'.format(date))
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(funcName)s: %(message)s')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

strem_handler = logging.StreamHandler()
strem_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(strem_handler)


def a():
    pass
#logger.info('Noice')
if __name__ == '__main__':
    notify2.init('break reminder', DBusGMainLoop())
    popup = notify2.Notification('Hour break', 'Its been an hour. Wanna take a break')
    popup.set_urgency(notify2.URGENCY_CRITICAL)
    i = 1
    PAUSE = False
    while True:
        sleep(10)
        if not PAUSE:
            popup.add_action('pause', 'pause', a)
            popup.add_action('rause', 'rause', a)

            if i % 3 == 0:
                popup.update('Hour break', 'Its been an hour. Wanna take a break')
            else:
                popup.update('20 minutes passed', 'Go for a stretch Dude')
            popup.set_timeout(1000)
            popup.show()
        popup.clear_actions()
        i = (i + 1) % 3
