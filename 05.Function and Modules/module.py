#Two types of module in python 1.external 2.build in module(math , os , etc)
import math
import my_module
import requests


print(math.sqrt(16))
my_module.hello()
r = requests.get("https://www.google.com")
print(r.text)