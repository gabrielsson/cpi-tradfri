import pygame as pg
from pytradfri.device import Device

class LightButton:

    def __init__(self, rect, light: Device):
        self.rect = pg.Rect(rect)
        self.light = light
        self.image = pg.Surface(self.rect.size).convert()
        
 
    def draw(self, surface):

        textColor = (83,83,83)

        if(self.light.reachable):
            if(self.light.light_control.lights[0].state):        
                self.image.fill((255,255,self.light.light_control.lights[0].dimmer/2))
            else: 
                self.image.fill((100,100,0))
        else: 
            self.image.fill((100,100,100))

        basicFont = pg.font.Font("skin/fonts/VarelaRound-Regular.ttf",16)
        text = basicFont.render(self.light.name, True, textColor)
        textRect = text.get_rect()
        textRect.centerx = self.rect.centerx 
        textRect.centery = self.rect.centery + self.rect.height / 2 + 14
        surface.blit(self.image, self.rect)
        lampImage = pg.image.load("skin/lamp_bg.png")
        surface.blit(lampImage.convert_alpha(), self.rect)
        surface.blit(text, textRect)
    
