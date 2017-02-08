from src.Actor import Actor

class FinnAndJake(Actor):

    # user defined
    def load(self):
        self.addAnimatedSprite('walk', "images/at.gif")
        self.addSprite('idle', 'images/at-idle.gif')
        self.centerAnchorPosition()
        self.setCurrentSprite('walk')

    def on_key_press(self, symbol, modifiers):
        if str(symbol) == '61':
            self.scale(2)
        elif str(symbol) == '45':
            self.scale(0.5)
        elif str(symbol) == '48':
            self.rotate(5)
        elif str(symbol) == '57':
            self.rotate(-5)
        elif str(symbol) == '65362':
            self.move(0, 10)
        elif str(symbol) == '65364':
            self.move(0, -10)

    def on_mouse_press(self, x, y, button, modifiers):
        for sprite in self.sprites:
            if self.sprites[sprite] != self.currentSprite:
                self.currentSprite = self.sprites[sprite]
                break