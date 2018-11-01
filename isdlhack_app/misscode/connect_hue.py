from phue import Bridge

b = Bridge('172.20.11.208')

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# Turn lamp 2 on
b.set_light(2,'on', True)

b.set_light(2,'on', True)
