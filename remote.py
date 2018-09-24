import sys
import pygame as pg
import logging
from LightApi import LightApi

from LightButton import LightButton
__author__ = "gabrielsson"
__copyright__ = "gabrielsson"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    pg.init()
    setup_logging()
    screen = pg.display.set_mode((320,240))
    done = False
    btns = []
    top = 25
    current = 0
    lightApi = LightApi()

    lights = lightApi.get_all_lights()


    for index, light in enumerate(lights):
        top = 26
        left = 51 * index
        btns.append(LightButton(rect=(left,top,50,70), light=light))

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                logging.error(event.key)
                if event.key == pg.K_LEFT:
                    if current == 0:
                        current = len(btns) - 1
                    else:
                        current -= 1
                if event.key == pg.K_RIGHT:
                    if current == len(btns) - 1:
                        current = 0
                    else:
                        current += 1
                if event.key == pg.K_UP:
                    lightApi.turn_on_light(btns[current].light)
                if event.key == pg.K_DOWN:
                    lightApi.turn_off_light(btns[current].light)
                elif event.key == pg.K_ESCAPE:
                    done = True
        for btn in btns:
            btn.draw(screen)
        btns[current].toggle(screen)
        pg.display.update()
    pg.quit()
def setup_logging():
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=logging.DEBUG, filename='./tradfri.log',
                        filemode='w',
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
    
if __name__ == '__main__':
    main()
    #sys.exit(main())
