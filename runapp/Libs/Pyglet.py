import pyglet

class Speaker():

    def play(self, filePath):
        pyglet.media.load(filePath).play()
