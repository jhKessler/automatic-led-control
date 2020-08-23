Automatic LED Controller

Implementation:


1: Go through the pyw files and follow all comments that are marked with a "##", filling them with your parameters

2: Open windows task scheduler by pressing the windows key and searching for "task scheduler"

3: Click on "create task" and name it


Turning leds off and on when sun is down:

4: Check box "run whether user is logged in or not" and configure for you operating system

5: Click on "trigger" and then "new"

6: Select "on startup" and check box for "repeat every:" and enter how often you want to check if leds should be turned on/off then click "ok"

7: Select the "action" menu and create a new action "start programm" and paste the path of your "automatic_led_control.pyw" file then click ok

8: Click ok to create the task


Turning leds off once you shutdown your pc:

4: Check box "run whether user is logged in or not" and configure for you operating system

5: Click on "trigger" and then "new"

6: Select "On Event" and enter following values: Log = System, Source = User32, EventID = 1074 then press ok

7: Select the "action" menu and create a new action "start programm" and paste the path of your "turn_off_on_sd.pyw" file then click ok


You are done! Your LEDs will now Turn on and off automatically once it gets dark out!



