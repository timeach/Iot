import paho.mqtt.client as mqtt
import time
from sense_hat import SenseHat
sense = SenseHat()
#set up mqtt client
client = mqtt.Client("pub1")
#set mqtt username/pw
client.username_pw_set(username="pi", password="123456")
#set server to publish to
client.connect("169.62.104.55", 1883)
client.loop_start()
try:
	while True:
#publish Barometric pressure to topic
		client.publish("sense/temp", "{:.2f}".format(sense.get_temperature()))
#publish temp to topic
		client.publish("sense/humid", "{:.2f}".format(sense.get_humidity()))
#publish humidity
		client.publish("sense/pressure", "{:.2f}".format(sense.get_pressure()))
#publish one button of joystick
		for event in sense.stick.get_events():
			client.publish("sense/stick", event.action)
#publish the magnetometer
		client.publish("sense/compass", "{:.2f}".format(sense.get_compass()))
#pause for 1 seconds
		time.sleep(1)
#deal nicely with ^C
except KeyboardInterrupt:
	print("interrupted!")
client.loop_stop()

