program that automatically turns on and off your led strips

steps to implement:


1: go through the pyw files and follow all comments that are marked with a "##" with your parameters

2: open windows task scheduler by pressing the windows key and searching for "task scheduler"

3: click on "create task" and name it


turning leds off and on when sun is down:
4: check box "run whether user is logged in or not" and configure for you operating system

5: click on "trigger" and then "new"

6: select "on startup" and check box for "repeat every:" and enter how often you want to check if leds should be turned on/off then click "ok"

7: select the "action" menu and create a new action "start programm" and paste the path of your "automatic_led_control.pyw" file then click ok

8: click ok to create the task

turning leds off once you shutdown your pc:

4: check box "run whether user is logged in or not" and configure for you operating system

5: click on "trigger" and then "new"

6: select "On Event" and enter following values: Log = System, Source = User32, EventID = 1074 then press ok

7: select the "action" menu and create a new action "start programm" and paste the path of your "turn_off_on_sd.pyw" file then click ok


You are done! Your LEDs will now Turn on and off automatically once it gets dark out!



