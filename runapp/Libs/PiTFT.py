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
time_font = pygame.font.SysFont("DejaVu Sans", 64)
date_font = pygame.font.SysFont("DejaVu Sans", 32)

screen.fill((0, 0, 0))        
now = datetime.datetime.now()
time_text = time_font.render(now.strftime("%H:%M:%S"), True, (128, 128, 128))
date_text = date_font.render(now.strftime("%d %B %Y"), True, (128, 128, 128))
screen.blit(time_text, (160 - time_text.get_width() // 2, 120 - time_text.get_height() // 2))
screen.blit(date_text, (0, 0)) 

pygame.display.update()

time.sleep(5)

