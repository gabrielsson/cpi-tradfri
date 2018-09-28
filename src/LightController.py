import pygame as pg

import lightapi
from pytradfri.device import Device
from LightButton import LightButton

class LightController: 
    btns = []
    current = 0
    def Init(self, screen): 
        self.lights = lightapi.get_all_lights()
        self.screen = screen
        for index, light in enumerate(self.lights):
            top = 15 + (95 * (index // 3))
            left = 95 * (index % 3) + 15
            btn =  LightButton(rect=(left,top,80,80), light=light)
            self.btns.append(btn)
            btn.draw(self.screen)
        
    def observe_callback(self, updated_device: Device):
        updated_device = Device
        for btn in self.btns:
            if btn.light.name == updated_device.name:
                btn.light = updated_device
                btn.draw(self.screen)

    def observe_err_callback(err):
        print('observe error:', err)


    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if self.current == 0:
                    self.current = len(self.btns) - 1
                else:
                    self.current -= 1
            if event.key == pg.K_RIGHT:
                if self.current == len(self.btns) - 1:
                    self.current = 0
                else:
                    self.current += 1
            if event.key == pg.K_UP:
                self.btns[self.current].light = lightapi.turn_on_light(self.btns[self.current].light)
            if event.key == pg.K_DOWN:
                self.btns[self.current].light = lightapi.turn_off_light(self.btns[self.current].light)
             
            for btn in self.btns:
                btn.draw(self.screen)
        self.btns[self.current].toggle(self.screen)
    
