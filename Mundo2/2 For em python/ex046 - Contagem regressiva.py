from time import sleep
from playsound import playsound
for x in range(10, -1, -1):
    sleep(1)
    print(x)
playsound('boom.mp3')
