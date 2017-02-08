class Frame(object):
    def __init__(self, name):
        self.name = name
        self.app = None
        self.window = None
        self.active = True
        self.actors = dict()
        self.frameVariables = dict()

    # user defined
    def load(self):
        pass

    def unload(self):
        pass

    # provided functions
    def setActive(self, active=True):
        if active and not self.active:
            self.active = True
        elif not active and self.active:
            self.active = False

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

    # no touch functions
    def on_activate(self):
        for actor in self.actors:
            self.actors[actor].load()
            self.window.push_handlers(self.actors[actor])
        self.load()

    def on_deactivate(self):
        self.unload()

    def on_draw(self):
        self.window.clear()
        for actor in self.actors:
            self.actors[actor].draw()

    # Pyglet window events
    # def on_close(self):
    #     pass
    #
    # def on_context_lost(self):
    #     pass
    #
    # def on_context_state_lost(self):
    #     pass
    #
    # def on_expose(self):
    #     pass
    #
    # def on_hide(self):
    #     pass
    #
    # def on_key_press(self, symbol, modifiers):
    #     pass
    #
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
    #
    # def on_mouse_press(self, x, y, button, modifiers):
    #     pass