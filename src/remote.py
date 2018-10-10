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
    controllerSurface = pg.Surface((320, 200))
    lightController = LightController()
    lightController.Init(controllerSurface)
    done = False
    header = getHeader()
    footer = getFooter()
    screen.blit(header, (0,0))
    screen.blit(footer, (0,220))
    pg.draw.line(screen,
            pg.Color(169, 169, 169),
            (0, screen.get_height() - 20),
            (screen.get_width(), screen.get_height() - 20),
            1)
    roundCorners(screen)
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                done = True
            lightController.get_event(event)
        lightController.draw_image_on_screen()
        screen.blit(controllerSurface, (0, 20))
        pg.display.update()
        clock.tick(30)
    pg.quit()

def getFooter():
    footer = pg.Surface((320, 20))
    footer.fill((255,255,255))
    return footer

def getHeader():
    header = getFooter()
    header.fill((120,120,120))
    basicFont = pg.font.SysFont(None, 16)
    textColor = (0,0,0)
    text = basicFont.render("Cpi Trådfri", True, textColor)
    header.blit(text, (14,4))
    return header


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
