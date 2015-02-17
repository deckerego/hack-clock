import os
import pygame
import time
import datetime

class Display():

    def __init__(self):
        os.putenv('SDL_FBDEV', '/dev/fb1')
        os.putenv('SDL_VIDEODRIVER', 'fbcon')

        pygame.display.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.time_font = pygame.font.SysFont("DejaVu Sans", 64)
        self.font_color = (128, 128, 128)

        self.hour = 0
        self.minute = 0
        self.second = 0
        self.colon = ":"
        self.evening = "AM"

    def setBrightness(self, level):
        self.font_color = (17 * level, 17 * level, 17 * level)

    def setColon(self, state=True):
        self.colon = ":" if state else " "

    def setEvening(self, state=True):
        self.evening = "PM" if state else "AM"

    def setMinutes(self, minutes):
        self.minute = minutes

    def setHours(self, hours):
        self.hour = hours

    def _update(self):
        screen.fill((0, 0, 0))
        time_text = time_font.render("%d%s%d %s" % (self.hour, self.colon, self.minute, self.evening), True, self.font_color)
        screen.blit(time_text, (160 - time_text.get_width() // 2, 120 - time_text.get_height() // 2))
        pygame.display.update()
