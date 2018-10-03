import sys
import pygame as pg
import logging

from LightController import LightController
__author__ = "gabrielsson"
__copyright__ = "gabrielsson"
__license__ = "mit"

_logger = logging.getLogger(__name__)
pg.init()
clock = pg.time.Clock()
roundcorners = pg.image.load("skin/roundcorners.png")


def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """

    setup_logging()
    screen = pg.display.set_mode((320, 240))
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
        lightController.draw_image_on_screen()
        pg.draw.line(screen, 
                pg.Color(169, 169, 169), 
                (0, screen.get_height() - 20), 
                (screen.get_width(), screen.get_height() - 20), 
                1)

        roundCorners(screen)
        pg.display.update()

        clock.tick(60)
    pg.quit()


def roundCorners(screen):
    screen.blit(roundcorners.convert_alpha(), (0, 0), (0, 0, 10, 10))
    screen.blit(roundcorners.convert_alpha(),
                (screen.get_width() - 10, 0), (0, 10, 10, 10))
    screen.blit(roundcorners.convert_alpha(),
                (0, screen.get_height() - 10), (0, 20, 10, 10))
    screen.blit(roundcorners.convert_alpha(), (screen.get_width() -
                                               10, screen.get_height() - 10), (0, 30, 10, 10))


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
