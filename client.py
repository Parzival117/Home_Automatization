# Importing modules
import time
import digitalio
import board

# import Adafruit IO REST client(you can use * to import all modules).
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Now giving each switch a feed to recieve data from

    #Establishing feed for relay 1
try: # if we have a 'relay1' feed
    relay1 = aio.feeds('relay1')
except RequestError: # create a relay1 feed
    feed = Feed(name="relay1")
    relay1 = aio.create_feed(feed)

    #Establishing feed for relay2
try: # if we have a 'relay2' feed
    relay2 = aio.feeds('relay2')
except RequestError: # create a relay2 feed
    feed = Feed(name="relay2")
    relay2 = aio.create_feed(feed)

    #Establishing feed for relay2
try: # if we have a 'relay2' feed
    relay2 = aio.feeds('relay2')
except RequestError: # create a relay2 feed
    feed = Feed(name="relay2")
    relay2 = aio.create_feed(feed)

    #Establishing feed for relay4
try: # if we have a 'relay4' feed
    relay4 = aio.feeds('relay4')
except RequestError: # create a relay4 feed
    feed = Feed(name="relay4")
    relay4 = aio.create_feed(feed)

# switch1 set up
switch1 = digitalio.DigitalInOut(board.D5)
switch1.direction = digitalio.Direction.OUTPUT

# switch2 set up
switch2 = digitalio.DigitalInOut(board.D6)
switch2.direction = digitalio.Direction.OUTPUT

# switch3 set up
switch3 = digitalio.DigitalInOut(board.D13)
switch3.direction = digitalio.Direction.OUTPUT

# switch4 set up
switch4 = digitalio.DigitalInOut(board.D19)
switch4.direction = digitalio.Direction.OUTPUT


while True:

    #Recieving data from feed and setting respective switch value
    data1 = aio.receive(relay1.key)
    if int(data1.value) == 1:
        print('relay1 <- ON\n')
    elif int(data1.value) == 0:
        print('relay1 <- OFF\n')

    data2 = aio.receive(relay2.key)
    if int(data2.value) == 1:
        print('relay1 <- ON\n')
    elif int(data2.value) == 0:
        print('relay1 <- OFF\n')

    data3 = aio.receive(relay3.key)
    if int(data3.value) == 1:
        print('relay1 <- ON\n')
    elif int(data3.value) == 0:
        print('relay1 <- OFF\n')

    data4 = aio.receive(relay4.key)
    if int(data4.value) == 1:
        print('relay1 <- ON\n')
    elif int(data4.value) == 0:
        print('relay1 <- OFF\n')



    # set the switches to the respective feed value
    switch1.value = int(data1.value)
    switch2.value = int(data2.value)
    switch3.value = int(data3.value)
    switch4.value = int(data4.value)

    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)
