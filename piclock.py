import pygame
from datetime import datetime
import threading
from clock_face import pi_clock_face


def run_clock():
    pygame.init()

    screen = pygame.display.set_mode((320,240))
    clock = pygame.time.Clock()
    pi_clock = pi_clock_face()
    done = False

    open_24_display_font = pygame.font.Font('open_24_display.ttf', 64)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
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


if __name__ == '__main__':
    run_clock()