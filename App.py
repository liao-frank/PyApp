import pyglet
from Frame import Frame
from Actor import Actor

class App(object):
    def __init__(self, name):
        self.name = name
        self.window = pyglet.window.Window()
        self.frames = dict()
        self.currentFrame = None
        self.appVariables = dict()

    def addFrame(self, frame):
        # add frame to frame data
        self.frames[frame.name] = frame
        # set the app and window in the frame
        frame.app = self
        frame.window = self.window

    def setFrame(self, name):
        self.window.clear()
        # setting the first frame
        if self.currentFrame == None:
            self.currentFrame = self.frames[name]
            self.window.push_handlers(self.currentFrame)
            return
        # pop all handlers
        try:
            self.window.pop_handlers()
            self.currentFrame.window.pop_handlers()
        except AssertionError:
            pass
        if self.currentFrame != None:
            self.currentFrame.on_deactivate()
        self.currentFrame = self.frames[name]
        self.window.push_handlers(self.currentFrame)
        self.currentFrame.on_activate()

    def setAppVariable(self, name, value):
        self.appVariables[name] = value

    def getAppVariable(self, name):
        if name in self.appVariables:
            return self.appVariables[name]
        return None

    def removeAppVariable(self, name):
        if name in self.appVariables:
            del self.appVariables[name]

    def run(self):
        pyglet.app.run()

myApp = App("myApp")

# create and add frames
testFrame = Frame("testFrame")
otherTestFrame = Frame("otherTestFrame")

myApp.addFrame(testFrame)
myApp.addFrame(otherTestFrame)
myApp.setFrame('testFrame')

# create an actor
at = Actor('finnAndJake')
at.addAnimatedSprite('walk', "at.gif")
at.addSprite('idle', 'at-idle.gif')
at.setCurrentSprite('walk')
testFrame.addActor(at)

myApp.run()