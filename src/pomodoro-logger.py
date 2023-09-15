#!/usr/bin/env python
"""
Description: Pomodoro Timer for a logfile
Version: 0.1
pomodoro-logger.py: A Python script (command-line interface) as a pomodoro timer ..
Development under Python 3.11.1 (venv)
"""
__author__: str = "Dietmar Fackelmann"
__email__: str = "github@nmit.de"
__license__: str = "GPLv3"

import logging
import time

pomodoro_log_version = 'pomodoro-logger.py Version 0.1.20230913-3'


# TODO Anzeige:
#  POMODORO 2/4
# "ACTION" oder "RELAX"
# aktuell
# [14.09.2023 10:13] focus time 29:20
# vorschlag
# [14.09.2023 10:13] pomo 2/4 *action*  relax  29:20
# [14.09.2023 10:13] pomo 3/4  action  *relax*  2:34
# möglich auch schreiben von 4 logs, die dann an unterschiedlichen Stellen positioniert werden können
# mit unterschiedlicher Größe ..
# [14.09.2023 10:13] pomo 2/4
# *produce*  relax
# 29:20
#
# entspannen / ausruhen / ruhe / erholung   / auszeit
# relax      / rest     / rest / recreation / time out
# produzieren / Aktion / Tätigkeit / Aufgabe / Auftrag / herstellen / beschäftigen / aktiv werden  / tun
# produce     / action / activity  /  task   / order   / produce    / employ       / become active / do
#
# Stream Words : study, studywithme, coworking, pomodoro,
# More to do : Tasks / Tasker erstellen
# IDEE: das ganze in Form eines Android Smartphones - und auch als App


def pomodoro(rounds, focustime, breaktime):
    inround = 0         # start with first round ..
    roundcounter = rounds
    logging.info('start ' + str(rounds) + ' pomodoro rounds (' + str(focustime) + 'm ' + str(breaktime) + 'm)')
    time.sleep(4)

    try:
        while rounds > 0:
            inround = inround + 1
            focustimer = (focustime * 60)  # set focustimer (number of minutes * 60 seconds)
            breaktimer = (breaktime * 60)  # set breaktime (number of minutes * 60 seconds)

            # logging.info('round ' + str(inround) + ' of ' + str(roundcounter))
            # time.sleep(2)
            rounds = rounds - 1
            # logging.info('prepare for focus time ..')
            # time.sleep(2)  # wait to x seconds to begin break time ..

            while focustimer:
                minutes = focustimer // 60
                seconds = focustimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + ' -> action <-   relax    ' + str(timer))
                time.sleep(1)
                focustimer = focustimer - 1
                logging.info(str(inround) + '/' + str(roundcounter) + '    action      relax    ' + str(timer))
                time.sleep(1)
                focustimer = focustimer - 1
            # logging.info('prepare for break time ..')
            # time.sleep(2)  # wait to x seconds to begin break time ..
            while breaktimer:
                minutes = breaktimer // 60
                seconds = breaktimer % 60
                timer = '{:02.0f}:{:02.0f}'.format(minutes, seconds)
                logging.info(str(inround) + '/' + str(roundcounter) + '    action  -> relax <-  ' + str(timer))
                time.sleep(1)
                breaktimer = breaktimer - 1
                logging.info(str(inround) + '/' + str(roundcounter) + '    action     relax     ' + str(timer))
                time.sleep(1)
                breaktimer = breaktimer - 1

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
    pomofocustime = 20      # set minutes to focus
    pomobreaktime = 5       # set minutes for break time
    pomodoro(pomorounds, pomofocustime, pomobreaktime)
