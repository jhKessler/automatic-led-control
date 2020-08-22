from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime

# define status of leds
with open("led_status.txt", "r") as status_file:
    led_status = status_file.read()
    leds_on = True if led_status == "on" else False

if leds_on:
    # turn off leds
    turn_off_leds() ## replace with your function for turning on your specific leds, i control my leds through pinging them via their local ip adress and giving them the parameters using the url
    # set up driver arguments for headless
    
    # define driver
    
    #options = Options()#
    #options.add_argument('--headless')#
    #options.add_argument("--disable-gpu")#
    #driver = webdriver.Firefox(options=options)#
    #URL = "http://#ip adress off leds, example: 192.168.1.2#/?red=0&green=0&blue=0"#
    #driver.get(URL)#
   
    action = "turned off"

else:
    action = "no action"


with open("detection_documentation.txt", "a") as documentation:
    documentation.write(f"Ran turn_off_leds at: {str(datetime.datetime.now())}" + f" | Status: {action}" + "\n")
