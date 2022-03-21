# Raspberry Pi B - Subscriber

### GPIO Pins
- GPIO(17): LED Yellow - Subscribes to topic "LightStatus"
- GPIO(23): LED Green - Subscribes to topic "Status/RaspberryPiA"
- GPIO(13): LED Red - Subscribes to topic "Status/RaspberryPiC"

### Install paho-mqtt on Raspberry Pi
`$ pip install paho-mqtt`

### Install gpiozero
`$ pip install gpiozero`

### Execute Code
1. Make sure raspberry pi is on same wifi as mqtt broker.
2. Change broker IP address in code line number 4.
3. Run `$ python rasp_pi_b.py`