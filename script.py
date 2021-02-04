import math
import sys
from os import rename

import requests


print(sys.version)
# # print(sys.executable)
def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet.title())
    print(greeting)


r = requests.get("https://binance.com")
print(r.status_code)
