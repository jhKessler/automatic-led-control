import datetime
import requests

# define led status
with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\led_status.txt", "r") as status_file:
    led_status = status_file.read()
    leds_on = True if led_status == "on" else False

if leds_on:
    # turn off leds
    URL = "http://192.168.178.30/?red=0&green=0&blue=0"
    #requests.get(URL)
    action = "turned off"

    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\led_status.txt", "w") as status_file:
        status_file.write("off")

else:
    action = "no action"


with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\detection_documentation.txt", "a") as documentation:
    time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    documentation.write(f"Ran turn_off_leds at: {time}" + f" | Status: {action}" + "\n")
