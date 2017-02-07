import pyglet

class Frame(object):
    def __init__(self, name):
        self.name = name
        self.app = None
        self.window = None
        self.actors = dict()
        self.frameVariables = dict()

    def load(self):
        pass

    def setActive(self, active=True):
        if active:
            self.window.push_handlers(self, 'frame')
        else:
            self.window.pop_handlers()

    def addActor(self, actor):
        self.actors[actor.name] = actor
        actor.window = self.window
        actor.frame = self

    def removeActor(self, name):
        if name in self.actors:
            del self.actors[name]

    def setFrameVariable(self, name, value):
        self.frameVariables[name] = value

    def getFrameVariable(self, name):
        if name in self.frameVariables:
            return self.frameVariables[name]
        return None

    def removeFrameVariable(self, name):
        if name in self.frameVariables:
            del self.frameVariables[name]

    # Pyglet window events
    def on_activate(self):
        for actor in self.actors:
            self.window.push_handlers(self.actors[actor])
        print("current frame switched to " + self.app.currentFrame.name)
    #
    # def on_close(self):
    #     pass
    #
    # def on_context_lost(self):
    #     pass
    #
    # def on_context_state_lost(self):
    #     pass
    #
    def on_deactivate(self):
      pass
    #
    def on_draw(self):
        self.window.clear()
        for actor in self.actors:
            self.actors[actor].draw()
    #
    # def on_expose(self):
    #     pass
    #
    # def on_hide(self):
    #     pass
    #
    def on_key_press(self, symbol, modifiers):
        print(self.name + " keyed " + str(symbol))
        # swap frames on SPACE
        if symbol == pyglet.window.key.SPACE:
            for frameName in self.app.frames:
                if frameName != self.name:
                    self.app.setFrame(frameName)
                    break
        elif symbol == pyglet.window.key.BACKSPACE:
            self.removeActor('frameLabel')
        return True

    # def on_key_release(self, symbol, modifiers):
    #     pass
    #
    # def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
    #     pass
    #
    # def on_mouse_enter(self, x, y):
    #     pass
    #
    # def on_mouse_leave(self, x, y):
    #     pass
    #
    # def on_mouse_motion(self, x, y, dx, dy):
    #     pass
    #
    # def on_mouse_press(self, x, y, button, modifiers):
    #     pass
    #
    # def on_mouse_release(self, x, y, button, modifiers):
    #     pass
    #
    # def on_mouse_scroll(self, x, y, dx, dy):
    #     pass
    #
    # def on_move(self, x, y):
    #     pass
    #
    # def on_resize(self, width, height):
    #     pass
    #
    # def on_show(self):
    #     pass
    #
    # def on_text(self, test):
    #     pass
    #
    # def on_text_motion(self, motion):
    #     pass
    #
    # def on_text_motion_select(self, motion):
    #     pass

    def on_mouse_press(self, x, y, button, modifiers):
        print(self.name + " clicked")
        return True