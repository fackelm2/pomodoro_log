#!/usr/bin/env python
"""
Description: Pomodoro Timer for a logfile
Version: 0.1
pomodoro-logger.py: A Python script (command-line interface) as a pomodoro timer ..
Development under Python 3.11.1 (venv)
"""
__version__: str = "0.1.20250405"
__author__: str = "Dietmar Fackelmann"
__email__: str = "github@nmit.de"
__license__: str = "GPLv3"

import logging
import time

pomodoro_log_version = 'pomodoro-logger.py Version 0.1.20250224'


def pomodoro(rounds, actiontime, relaxtime):
    inround = 0         # start with first round ..
    roundcounter = rounds
    logging.info('start ' + str(rounds) + ' pomodoro rounds (' + str(actiontime) + 'm ' + str(relaxtime) + 'm)')
    time.sleep(4)

    try:
        while rounds > 0:
            inround = inround + 1
            actiontimer = (actiontime * 60)  # set actiontimer (number of minutes * 60 seconds)
            relaxtimer = (relaxtime * 60)  # set relaxtime (number of minutes * 60 seconds)

            # logging.info('round ' + str(inround) + ' of ' + str(roundcounter))
            # time.sleep(2)
            rounds = rounds - 1
            # logging.info('prepare for action time ..')
            # time.sleep(2)  # wait to x seconds to begin break time ..

            while actiontimer:
                minutes = actiontimer // 60
                seconds = actiontimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + ' -> action <-   relax    ' + str(timer))
                time.sleep(1)

                actiontimer = actiontimer - 1

                minutes = actiontimer // 60
                seconds = actiontimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + '    action      relax    ' + str(timer))
                time.sleep(1)
                actiontimer = actiontimer - 1
            # logging.info('prepare for break time ..')
            # time.sleep(2)  # wait to x seconds to begin break time ..
            while relaxtimer:
                minutes = relaxtimer // 60
                seconds = relaxtimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + '    action  -> relax <-  ' + str(timer))
                time.sleep(1)

                relaxtimer = relaxtimer - 1

                minutes = relaxtimer // 60
                seconds = relaxtimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + '    action     relax     ' + str(timer))
                time.sleep(1)
                relaxtimer = relaxtimer - 1

        logging.info('pomodoro finished ..')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    # log file configuration
    loggingformat = '[%(asctime)s] %(message)s'
    # logging.basicConfig(filename='pomodoro.log', encoding='utf-8', level=logging.DEBUG, format=loggingformat,
    #                   datefmt='%Y-%m-%d %H:%M')
    logging.basicConfig(filename='pomodoro.log', encoding='utf-8', level=logging.DEBUG, format=loggingformat,
                        datefmt='%d.%m.%Y %H:%M')
    print('pomodoro-logger.py writes timer in file \"pomodoro.log\" for integration in OBS ..')
    pomorounds = 4          # set number of pomodoro rounds ..
    pomoactiontime = 50      # set minutes to focus
    pomorelaxtime = 10       # set minutes for break time
    pomodoro(pomorounds, pomoactiontime, pomorelaxtime)

# todo
# watch actual time and make pomodoro break at 12:00 - 13:00 for lunch and breake
# choose best pomodoro timer for
# first possible start time (for example 9:00) and last end  time at (for example at 20:00)