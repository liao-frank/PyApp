import pyglet
from src.Frame import Frame

class TestFrame(Frame):
    def __init__(self, name):
        self.name = name
        self.app = None
        self.window = None
        self.active = True
        self.actors = dict()
        self.frameVariables = dict()

    def load(self):
        print("current frame: (" + self.name + ")")

    def unload(self):
        pass

    def on_key_press(self, symbol, modifiers):
        print("frame (" + self.name + ") heard a key: " + str(symbol))
        # swap frames on SPACE
        if symbol == pyglet.window.key.SPACE:
            for frameName in self.app.frames:
                if frameName != self.name:
                    self.app.setFrame(frameName)
                    break
        elif symbol == pyglet.window.key.BACKSPACE:
            self.removeActor('frameLabel')
        return True

    def on_mouse_press(self, x, y, button, modifiers):
        print("frame (" + self.name + ") heard a click")