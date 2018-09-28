import sys
import pygame as pg
import logging

from LightController import LightController
__author__ = "gabrielsson"
__copyright__ = "gabrielsson"
__license__ = "mit"

_logger = logging.getLogger(__name__)
pg.init()


def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """

    setup_logging()
    screen = pg.display.set_mode((320,240))
    lightController = LightController()
    lightController.Init(screen)
    done = False
    top = 25
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                done = True  
            lightController.get_event(event)
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