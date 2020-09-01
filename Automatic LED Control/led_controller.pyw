import datetime
from bs4 import BeautifulSoup
import requests

def get_suntimes():

    # url of sunset and sunrise website
    URL = "https://sunrisesunset.de/sonne/deutschland/hamburg/"

    # get values of sunset and sunrise
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, "html.parser")

    sunset_str = soup.find(id="sunset").text
    sunrise_str = soup.find(id="sunrise").text
    
    minutes_offset = 30
    sunset =  (datetime.datetime.strptime(sunset_str, '%H:%M') - datetime.timedelta(minutes=minutes_offset)).time()
    sunrise =  (datetime.datetime.strptime(sunrise_str, '%H:%M') + datetime.timedelta(minutes=minutes_offset)).time()

    return sunset, sunrise


def get_led_status():
    
    # define led status right now and return it
    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\led_status.txt", "r") as status_file:
        led_status_str = status_file.read()
        led_status = True if led_status_str == "on" else False
    
    return led_status


def check_dark_out(sun_times):
    
    (sunset, sunrise) = sun_times

    # define conditions to find out if time right now is between sunset and sunrise using midnight
    on_condition1 = True if sunset < now < midnight1 else False
    on_condition2 = True if midnight2 < now < sunrise else False
    
    dark_out = True if on_condition1 or on_condition2 else False

    return dark_out


def check_action(led_status, dark_out):

    # check which action to take and define it for the documentation
    if dark_out and not led_status:
        turn_on_leds()
        action = "turned on leds"

    elif not dark_out and led_status:
        turn_off_leds()
        action = "turned off leds"

    else:
        action = False
    return action


def turn_on_leds():
    
    # define rgb value of led
    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\VALUES.txt", "r") as values_file:
        content = values_file.read().split(":")
        red, green, blue = content[0], content[1], content[2]
        
    # turn on leds
    rgb_url = f"http://192.168.178.30/?red={red}&green={green}&blue={blue}"
    # requests.get(rgb_url)

    # change led status to on
    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\led_status.txt", "w") as status_file:
        status_file.write("on")


def turn_off_leds():
    
    off_url = "http://192.168.178.30/?red=0&green=0&blue=0"
    # requests.get(off_url)
    
    # change status of leds to off
    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\led_status.txt", "w") as status_file:
        status_file.write("off")


def write_documentation(action):
    # add time documentation to file
    with open(r"C:\Users\Johnny\Desktop\Automatisierung\data\detection_documentation.txt", "a") as documentation:
        documentation.write(f"Ran led_detection at: {now} | Status: {action}" + "\n")


# define times
now = datetime.datetime.now().time()

midnight1 = datetime.time(hour=23, minute=59)
midnight2 = datetime.time()

threeAM = datetime.time(hour=3)
tenAM = datetime.time(hour=10)
threePM = datetime.time(hour=15)

# times the sun is defintely up or down so the program doesnt need to run if the leds alreadyy have the right status
led_status = get_led_status()

nighttime = True if midnight2 < now < threeAM and led_status else False
daytime = True if tenAM < now < threePM and not led_status else False

runtime = True if not daytime and not nighttime else False

# run program
if runtime:
    # get times for sunset/sunrise and check if its dark out 
    dark_out = check_dark_out(get_suntimes())

    # run program and define documentation
    action = check_action(led_status, dark_out)

    if action:
        # write documentation
        write_documentation(action)
