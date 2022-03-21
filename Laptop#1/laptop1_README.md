# Laptop 1 - MQTT Broker

### Install mosquitto via homebrew
`$ brew install mosquitto`

### Instructions for allowing unauthenticated access on Mac
1. Edit mosquitto.conf (/opt/homebrew/etc/mosquitto/mosquitto.conf)
2. Uncomment `allow_anonymous false`, change it to `allow_anonymous true`
3. Add `listener 1883` above `allow_anonymous true`

### Run mosquitto broker with customized config file
`$ /opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf`