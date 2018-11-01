import sys
from phue import Bridge

#username : rwm9ymUfYdNgNJP5oONJePaam7bnqUBfgPRBrm1O
b = Bridge('172.20.11.208')
lights = b.get_light_objects('2')

HUE = int(150)

lights[1].on = True
lights[1].brightness = HUE
