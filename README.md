This is the among us taskmaster. It can complete almost every task in the first map of the game among us.

///// Almost every pixel coordinates are completely hardcoded since I just made it for my own use. So, it can only run on the screen resolution of 1920x1080 and while the game is on fullscreen. /////

The tasks that it cannot complete are:

1. Clean O2 Filter
2. Unlock Manifolds
3. Start Reactor
4. Clear Asteroids

To use the taskmaster, open the _main.py file and wait for it to load. Go to among us and play in fullscreen mode. Press the "r" key after opening a task.
There is a "key" variable in the _main.py file which is set to "r" on default. But it can be changed to any key on keyboard as per the requirement.

The code is divided into 3 files, the detector, the performer and the main file.

The detector is obviously going to actually detect which task should it should perform. For this, it matches the color value of 1-3 hardcoded pixel locations until 
it recognizes the task. It is not recommended to run the program outside of among us because it can rarely give false positives and may move your mouse around uncontrollably.

The performer is the file that performs the task itself. Every task has a different code some simple (like download/upload) and some complex (like clean vent).

The program may not perform some tasks correctly while being sabotaged due to the red flashing on the screen.

There is also a data folder which stores the screenshot of some tasks where direct image recognition is required (like clean vent, align engine output, chart course).
