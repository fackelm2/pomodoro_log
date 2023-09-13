# pomodoro_logger (BETA)

## command line tool to write pomodoro timer in text file (log file)
A simple command-line tool because i needed a fast solution for a pomodoro timer. <br>
So I used the python loggging mechanismen to write the pomodoro timer in a log file.<br>

You can change the number of rounds, the focus time (minutes) and the break time (minutes) by changing the following constants in the python script in the main() part:

```sh
pomorounds = 4          # set number of pomodoro rounds ..
pomofocustime = 30      # set minutes to focus
pomobreaktime = 5       # set minutes for break time
```

The script generates the log file "pomodoro.log" and write every second of the timer in this log. 
You can also evaluate the log later or use it as a working time log.

## OBS configuration
a) add "Text(GDI+)" to a "OBS Szene"<br>
b) activate "Aus Datei lesen"<br>
c) choose "pomodoro.log" file from you location of the python script<br>

## Start pomodoro timer
start python script
```
# python pomodoro-logger.py
```

the script will automatically start to write the 
pomodoro.log file in the same directory of the script.
