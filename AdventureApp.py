from src.App import App
from FinnAndJake import FinnAndJake
from TestFrame import TestFrame

myApp = App("myApp")

# create and add frames
testFrame = TestFrame("testFrame")
otherTestFrame = TestFrame("otherTestFrame")

myApp.addFrame(testFrame)
myApp.addFrame(otherTestFrame)
myApp.setFrame('testFrame')

# create an actor
at = FinnAndJake('finnAndJake')
testFrame.addActor(at)

myApp.run()