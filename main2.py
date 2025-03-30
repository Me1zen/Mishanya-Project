from pygame import*

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.rect.x += self.speed

        super().update(screen)

class Background(GameSprite):
    def __init__(self,image_name, x, y, width, height, speed):
        super().__init__(image_name, x, y, width, height, speed)

    def update(self, screen):
        self.rect.y += self.speed
        if self.rect.y >= WINDOW_HEIGHT:
            self.rect.y = 0 - self.rect.height

        super().update(screen)

class Map:
    def __init__(self):
        self.background1 = Background("background.png", 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 5)
        self.background2 = Background("background.png",0, -WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, 5)

    def update(self, screen):
        self.background1.update(screen)
        self.background2.update(screen)


window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT,))

player = Player("SpaceshipShooterGodot/Player/ship.png", 5, 400, 70, 100, 10)
clock = time.Clock()

map = Map()

clock = time.Clock()

run = True
menu = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    map.update(window)

    player.update(window)

    display.update()
    clock.tick(FPS)