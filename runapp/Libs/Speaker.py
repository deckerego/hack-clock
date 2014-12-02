#!/usr/bin/env python

import pygame

class Speaker():

    def __init__(self):
        pygame.init()

    def __del__(self):
        pygame.quit()

    def play(self, filePath):
        pygame.mixer.Sound(filePath).play()
