import os
import pygame
import time
import datetime

os.putenv('SDL_FBDEV', '/dev/fb1') 
os.putenv('SDL_VIDEODRIVER', 'fbcon')

pygame.display.init()
pygame.font.init()
pygame.mouse.set_visible(False)
    
size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill((0, 0, 0))        
pygame.display.update()

font = pygame.font.SysFont("comicsansms", 96)
now = datetime.datetime.now()
text = font.render("%d:%d:%d" % (now.hour, now.minute, now.second), True, (128, 128, 128))
screen.blit(text, (160 - text.get_width() // 2, 120 - text.get_height() // 2))

pygame.display.update()

time.sleep(5)

