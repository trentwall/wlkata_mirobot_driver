# wlkata_mirobot_driver
This is a python code that interfaces with wlkata mirobot and text files. The purpose of this code is to act an driver that will allow users to write your own api for the wlkata mirobot 6axis robot arm, in any langauge that can read and write to text files.  

To use: git clone this repo,
./mirobotdriver.py

To send commands to the robot: check that the first char in the file is "^". Then, modify the first line of the input.txt file. Be sure to add a newline at the end of the command.

The output from the mirobot is stored in mirobot_response.txt.

The serial interface for this code is miniterm.py at https://github.com/pyserial/pyserial/blob/master/serial/tools/miniterm.py. The interface has been changed to work with the wlkata mirobot. This code is provided as is.
