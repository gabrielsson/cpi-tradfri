import pygame as pg
from LightApi import LightApi
from pytradfri.device import Device

class LightButton:
    lightApi = LightApi()

    def __init__(self, rect, light: Device):
        self.rect = pg.Rect(rect)
        self.light = light
        self.image = pg.Surface(self.rect.size).convert()
        self.draw(self.image)
        
 
    def draw(self, surface):
        basicFont = pg.font.SysFont(None, 16)
        text = basicFont.render(self.light.name, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.centerx = self.rect.centerx
        textRect.centery = self.rect.centery

        if(self.light.reachable):
            if(self.light.light_control.lights[0].state):
                self.image.fill((255,0,0))
            else: 
                self.image.fill((100,0,0))
        else: 
            self.image.fill((100,100,100))
        surface.blit(self.image, self.rect)

        surface.blit(text, textRect)
    
    def toggle(self, surface):
        toggle = pg.Surface(self.rect.size).convert()
        toggle.fill((0,0,255))
        surface.blit(toggle, self.rect)