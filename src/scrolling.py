import sys

import pygame as pg


class Game(object):
    def __init__(self, screen_size):
        self.done = False
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.bg_size = 2000, 720
        #the original background image
        self.bg_image = pg.Surface(self.bg_size)
        self.bg_image.fill(pg.Color("gray5"))
        pg.draw.circle(self.bg_image, pg.Color("red"), (500, 300), 100)
        pg.draw.circle(self.bg_image, pg.Color("blue"), (1000, 500), 100)
        pg.draw.circle(self.bg_image, pg.Color("green"), (1100, 300), 100)
        pg.draw.circle(self.bg_image, pg.Color("purple"), (1850, 200), 100)
        #the surface we'll actually draw to the screen as the background
        self.bg = pg.Surface(screen_size)
        #this rect will track what portions of the background need to be drawn
        self.bg_rect = self.bg.get_rect()
        
        self.scroll_time = 10 #move background 1 pixel every 10 milliseconds
        self.timer = 0

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self, dt):
        self.timer += dt
        while self.timer >= self.scroll_time:
            self.timer -= self.scroll_time
            self.bg_rect.left += 1

        if self.bg_rect.left >= self.bg_size[0]:
            self.bg_rect.left = self.bg_rect.left - self.bg_size[0]
        if self.bg_rect.right > self.bg_size[0]:
            left_rect = pg.Rect(self.bg_rect.topleft, 
                    (self.bg_size[0] - self.bg_rect.left, self.bg_rect.height))
            right_rect = pg.Rect(0, self.bg_rect.top,
                    self.bg_rect.right - self.bg_size[0], self.bg_rect.height)
            left = self.bg_image.subsurface(left_rect)
            right = self.bg_image.subsurface(right_rect)
            self.bg.blit(left, (0, 0))
            self.bg.blit(right, (left_rect.width, 0))
        else:
            subsurf = self.bg_image.subsurface(self.bg_rect) 
            self.bg.blit(subsurf, (0, 0))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


if __name__ == "__main__":
    game = Game((1280, 720))
    game.run()
    pg.quit()
    sys.exit()