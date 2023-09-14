# pomodoro-logger (BETA)

## command line tool to write pomodoro timer in text file (log file)
A simple command-line tool because i needed a fast solution for a pomodoro timer while streaming with OBS. <br>
See the example_pictures-001.jpg for example. The Timer ist on the left upper corner. <br>

I used the python loggging mechanismen to write the pomodoro timer in a log file.<br>

Attention: The logfile will grow (one entry every second) while executing this script.<br>

You can change the number of rounds, the focus time (minutes) and the break time (minutes) by changing the following constants in the python script in the main() part:

```sh
pomorounds = 4          # set number of pomodoro rounds ..
pomofocustime = 30      # set minutes to focus
pomobreaktime = 5       # set minutes for break time
```

The script generates the log file "pomodoro.log". <br>
You can use the log file as a working time log or evaluate your focus times.

## OBS configuration
First execute the script a few seconds to generate the log file the first time.<br>
Start OBS an choose your "Szene" to add the pomodoro counter<br>
a) add "Text(GDI+)" to a "OBS Szene"<br>
b) activate "Aus Datei lesen"<br>
c) choose "pomodoro.log" file from you location of the python script <br>

## Start pomodoro timer
start python script
```
# python pomodoro-logger.py
```

the script will automatically start to write the timer data line for line<br> 
in the file "pomodoro.log" in the same directory of the script:
```
# more pomodoro.log
[13.09.2023 23:10] start 4 pomodoro rounds (30m 5m)
[13.09.2023 23:10] round number 1 of 4
[13.09.2023 23:10] focus time 30:00
[13.09.2023 23:10] focus time 29:59
[13.09.2023 23:10] focus time 29:58
[13.09.2023 23:10] focus time 29:57
[13.09.2023 23:10] focus time 29:56
[13.09.2023 23:10] focus time 29:55
...
```
