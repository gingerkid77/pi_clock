import pygame
from datetime import datetime
import threading
from clock_face import pi_clock_face
import os
from num2words import num2words


def run_clock():
    # this works to display on the TFT
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ['SDL_MOUSEDRV'] = 'TSLIB'
    os.environ['SDL_MOUSEDEV'] = '/dev/input/mouse0'

    clock_ticks = 10

    pygame.init()

    screen = pygame.display.set_mode((320, 240))
    clock = pygame.time.Clock()
    pi_clock = pi_clock_face(clock_surface=pygame.Surface((320,240)),fade_speed=clock_ticks)
    done = False

    while not done:

        for event in pygame.event.get():
            # print(str(event))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pi_clock.kill_clock()
                elif event.key == pygame.K_SPACE:
                    print('space pressed')
                    pi_clock.reset_clock()

        screen.fill((0, 0, 0))

        screen.blit(pi_clock.draw_clock(), (0, 0))

        pygame.display.flip()
        clock.tick(clock_ticks)


if __name__ == '__main__':
    run_clock()
