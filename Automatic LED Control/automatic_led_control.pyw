import datetime
import requests
from bs4 import BeautifulSoup

# url of sunset and sunrise website
URL = "https://sunrisesunset.de/sonne/deutschland/hamburg/" ## edit url for your area

# check sunset function
def check_sunset():
    
    # get values of sunset and sunrise
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, "html.parser")
    
    sunset_str = soup.find(id="sunset").text
    sunrise_str = soup.find(id="sunrise").text

    # define sunset and sunrise time
    minutes_offset = 30 # i want the leds to turn on when its just starting to get dark out and off when the sun is completely up, feel free to change to your wishes
    sunset =  (datetime.datetime.strptime(sunset_str, '%H:%M') - datetime.timedelta(minutes=minutes_offset)).time()
    sunrise =  (datetime.datetime.strptime(sunrise_str, '%H:%M')+ datetime.timedelta(minutes=minutes_offset)).time()

    # define conditions to find out if time right now is between sunset and sunrise using midnight
    on_condition1 = True if sunset < now < midnight1 else False
    on_condition2 = True if midnight2 < now < sunrise else False
    dark_out = True if on_condition1 or on_condition2 else False

    # define led status right now
    with open("led_status.txt", "r") as status_file:
        led_status_str = status_file.read()
        led_status = True if led_status_str == "on" else False

    # if time is between sunset and sunrise and led is not turned on, turn on the leds
    if dark_out and not led_status:
        # define rgb value of led
        with open("values.txt", "r") as values_file:
            content = values_file.read().split(":")
            red, green, blue = content[0], content[1], content[2]
        
        # turn on leds
        turn_on_leds() ## replace with your function for turning on your specific leds, i control my leds through pinging them via their local ip address and giving them the parameters using the url
        """
        rgb_url = f"http://#ip adress off leds, example: 192.168.1.2#/?red={red}&green={green}&blue={blue}"
        request.get(rgb_url)
        """
        # change led status to on
        with open("led_status.txt", "w") as status_file:
            status_file.write("on")

        # define action for documentation
        action = "turned on leds"
        
    # if time is not between sunset and sunrise and led is turned on, turn off the leds
    elif not on_condition1 and not on_condition2 and led_status:
        turn_off_leds() ## enter your function for turning off your specific leds here, i control my leds through pinging them via their ip adress and giving them the parameters using the url
        """        
        off_url = "http://#ip adress off leds, example: 192.168.1.2#/?red=0&green=0&blue=0""
        requests.get(off_url)
        """
        # change status of leds to off
        with open("led_status.txt", "w") as status_file:
            status_file.write("off")

        # define action for documentation
        action = "turned off leds"

    else:
    # define action for documentation
        action = "no action"
    # change time documentation for last run
    with open("detection_documentation.txt", "a") as documentation:
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        documentation.write("Ran led_detection at: " + time + f" | Status: {action}" + "\n")

# get time right now
now = datetime.datetime.now().time()

# define midnight and 3am
midnight1 = datetime.time(hour=23, minute=59)
midnight2 = datetime.time()
threeAM = datetime.time(hour=3)
# call the program
nighttime = True if midnight2 < now < threeAM else False

if not nighttime:
    check_sunset()




