import pygame as pg

import lightapi
from pytradfri.device import Device
from LightButton import LightButton


class LightController:
    btns = []
    current = 0
    selectorImage = pg.image.load("skin/blueselector.png")

    def Init(self, screen):
        self.screen = screen
        self.lights = lightapi.get_all_lights()
        self.bg_size = len(self.lights) * 100 + 40, screen.get_height()
        if self.bg_size[0] < screen.get_width():
            self.bg_size = screen.get_width(), screen.get_height()
        self.bg_image = pg.Surface(self.bg_size)
        self.bg_image.fill(pg.Color("white"))

        for index, light in enumerate(self.lights):
            top = 40 if self.current == index else 60
            left = 100 * index + 20
            btn = LightButton(rect=(left, top, 80, 80), light=light)
            self.btns.append(btn)
            btn.draw(self.bg_image)

        self.bg_rect = self.screen.get_rect()
        subsurf = self.bg_image.subsurface(self.bg_rect)
        self.screen.blit(subsurf, (0, 0))

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.bg_image.fill(pg.Color("white"))
            if event.key == pg.K_LEFT:
                if self.current > 0:
                    self.current -= 1
            if event.key == pg.K_RIGHT:
                if self.current < len(self.btns) - 1:
                    self.current += 1
            if event.key == pg.K_UP:
                self.btns[self.current].light = lightapi.turn_on_light(
                    self.btns[self.current].light)
            if event.key == pg.K_DOWN:
                self.btns[self.current].light = lightapi.turn_off_light(
                    self.btns[self.current].light)

            for index, btn in enumerate(self.btns):
                btn.rect.top = 60
                if index == self.current:
                    btn.rect.top = 40
                btn.draw(self.bg_image)

    def draw_image_on_screen(self):
        self.mark_icon()

        if self.current < len(self.btns) - 1 and self.current > 0:
            if self.bg_rect.left < (self.current - 1) * 100:
                self.bg_rect.left += 10
            elif self.bg_rect.left > (self.current - 1) * 100:
                self.bg_rect.left -= 10


        subsurf = self.bg_image.subsurface(self.bg_rect)
        self.screen.blit(subsurf, (0, 0))

    def mark_icon(self):

        top = 34
        left = 100 * self.current + 14
        rect = (left, top, 80, 80)
        self.bg_image.blit(self.selectorImage.convert_alpha(), rect)
