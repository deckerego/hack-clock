import pygame

class Speaker():

    def __init__(self):
        pygame.init()

    def __del__(self):
        pygame.quit()

    def play(self, filePath):
        filePath = "../runapp/audio/%s" % fileName
        pygame.mixer.Sound(filePath).play()
