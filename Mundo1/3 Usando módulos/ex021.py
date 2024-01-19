import pygame
import time
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("boom.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
time.sleep(11)
print('OK')