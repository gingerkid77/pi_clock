import pygame
from datetime import datetime
import threading
from clock_face import pi_clock_face
import os
from pitftgpio import PiTFT_GPIO


def run_clock():
    # this works to display on the TFT
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ['SDL_MOUSEDRV'] = 'TSLIB'
    os.environ['SDL_MOUSEDEV'] = '/dev/input/mouse0'

    pitft = PiTFT_GPIO()

    pygame.init()

    screen = pygame.display.set_mode((320,240))
    clock = pygame.time.Clock()
    pi_clock = pi_clock_face()
    done = False

    open_24_display_font = pygame.font.Font('open_24_display.ttf', 64)

    while not done:

        if pitft.Button1:
            print('Button 1 pressed')
        if pitft.Button2:
            print('Button 2 pressed')
        if pitft.Button3:
            print('Button 3 pressed')
        if pitft.Button3:
            print('Button 4 pressed')

        for event in pygame.event.get():
            # print(str(event))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pi_clock.kill_clock()
                elif event.key == pygame.K_SPACE:
                    print('space pressed')
                    pi_clock.reset_clock()

        text = open_24_display_font.render(datetime.now().strftime("%H:%M:%S"), 
        True, 
        pi_clock.get_curr_clock_colour())

        screen.fill((0,0,0))
        screen.blit(text,
            ((320 - text.get_width()) / 2, (240 - text.get_height()) / 2))
        
        pygame.display.flip()
        clock.tick(60)
        print('tick')

if __name__ == '__main__':
    run_clock()