# Utilities
Different useful scripts that don't fit the other categories.

## Melody assign
**This script requiers termcolor**

This script was originally created for a game between friends, each one writes a small melody and these are distributed randomly, I kept it because it could be usefull for other situations.
To use it you write the names of the participants in composers.txt, and then run the script in the terminal.

    $ python melody_assign.py
    Neelam Clay: Iram Medina's idea
    Iram Medina: Heidi Hale's idea
    Heidi Hale: Angelica Powers's idea
    Rares Holding: Marian Andersen's idea
    Angelica Powers: Izabela Fellows's idea
    Marian Andersen: Terrell Whitley's idea
    Freja Sosa: Rares Holding's idea
    Izabela Fellows: Freja Sosa's idea
    Terrell Whitley: Cieran Conrad's idea
    Cieran Conrad: Neelam Clay's idea

## Task Assign
**This script is unfinished**

**This script requiers termcolor**

Similar to Melody Assign this is scipt can be used to randomly assign tasks to people, to use it you type the names of the participants under People in list.txt, and the names of the tasks under Tasks.

    $ python task_assign.py
    Do the laundry: Samira Choi
    Wash the dishes: Jaylen Rosa
    Clean the house: Corey Senior
    Cook: Jaylen Rosa
    Do the shopping: Corey Senior

_This script still WIP, because the names may repeat on the tasks, i'll fix it when i have time._

---
## Pomodor
**This script requires PyGame**

This is a pomodoro timer, to use it you run the script in the terminal and it will asks for the session and rest time (in minutes) and the number of sessions, after that the timer will start and play a sound when it finishes.

    $python pomodor.py
    insert session time: 1
    insert rest time: 1
    insert sessions number: 1
    session 1
    1:00
    Rest time!
    1:00
    session ended