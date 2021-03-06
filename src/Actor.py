import pyglet

class Actor(object):
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.window = None
        self.frame = None
        self.sprites = dict()
        self.currentSprite = None
        self.actorVariables = dict()
        self.x0 = x
        self.y0 = y
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    # user defined
    def load(self):
        pass

    # provided functions
    def delete(self):
        # delete all stored sprites
        for sprite in self.sprites:
            self.sprites[sprite].delete()

    def setActive(self, active=True):
        if active and not self.active:
            self.active = True
        elif not active and self.active:
            self.active = False

    def addSprite(self, name, imagePath):
        image = pyglet.image.load(imagePath)
        
        sprite = pyglet.sprite.Sprite(image)
        sprite.set_position(self.x, self.y)

        self.sprites[name] = sprite

    def addAnimatedSprite(self, name, imagePath):
        animation = pyglet.image.load_animation(imagePath)

        bin = pyglet.image.atlas.TextureBin()
        animation.add_to_texture_bin(bin)
        sprite = pyglet.sprite.Sprite(animation)
        sprite.set_position(self.x, self.y)

        self.sprites[name] = sprite

    def setCurrentSprite(self, name):
        if name in self.sprites:
            self.currentSprite = self.sprites[name]

    def removeSprite(self, name):
        if name in self.sprites:
            del self.sprites[name]

    def setActorVariable(self, name, value):
        self.actorVariables[name] = value

    def getActorVariable(self, name):
        if name in self.actorVariables:
            return self.actorVariables
        return None

    # transformations and translations
    def getMaxWidth(self):
        max = 0
        for sprite in self.sprites:
            image = self.sprites[sprite].image
            if isinstance(image, pyglet.image.AbstractImage):
                if image.width > max:
                    max = image.width
            elif isinstance(image, pyglet.image.Animation):
                if image.get_max_width() > max:
                    max = image.get_max_width()
        return max

    def getMaxHeight(self):
        max = 0
        for sprite in self.sprites:
            image = self.sprites[sprite].image
            if isinstance(image, pyglet.image.AbstractImage):
                if image.height > max:
                    max = image.height
            elif isinstance(image, pyglet.image.Animation):
                if image.get_max_height() > max:
                    max = image.get_max_height()
        return max

    def move(self, dx, dy):
        for sprite in self.sprites:
            self.sprites[sprite].x += dx
            self.sprites[sprite].y += dy
            assert(self.sprites[sprite].position == (self.sprites[sprite].x, self.sprites[sprite].y))

    def setPosition(self, x, y):
        for sprite in self.sprites:
            self.sprites[sprite].position = (x, y)

    def centerAnchorPosition(self):
        for sprite in self.sprites:
            image = self.sprites[sprite].image
            if isinstance(image, pyglet.image.AbstractImage):
                image.anchor_x = image.width // 2
                image.anchor_y = image.height // 2
            elif isinstance(image, pyglet.image.Animation):
                for frame in image.frames:
                    frameImage = frame.image
                    frameImage.anchor_x = frameImage.width // 2
                    frameImage.anchor_y = frameImage.height // 2
        # adjust position
        self.move(self.getMaxWidth() // 2, self.getMaxHeight() // 2)


    def scale(self, factor):
        for sprite in self.sprites:
            self.sprites[sprite].scale *= factor

    def setScale(self, scale):
        for sprite in self.sprites:
            self.sprites[sprite].scale = scale

    def rotate(self, dtheta):
        for sprite in self.sprites:
            self.sprites[sprite].rotation += dtheta

    def setRotation(self, theta):
        for sprite in self.sprites:
            self.sprites[sprite].rotation = theta

    # no touch functions

    def on_draw(self):
        self.currentSprite.draw()

    # Pyglet window events
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