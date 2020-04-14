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
    pi_clock = pi_clock_face(clock_ticks)
    done = False

    open_24_display_font = pygame.font.Font('DIN.ttf', 20)

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

        curr_time = datetime.now()

        screen.fill((0, 0, 0))

        minute_text = 'exactly'
        hour_text = 'midnight'

        if curr_time.minute == 0:
            minute_text = 'exactly'
        elif curr_time.minute < 30:
            if curr_time.minute == 15:
                minute_text = 'quarter past'
            else:
                minute_text = num2words(curr_time.minute) + ' minutes past'
        elif curr_time.minute == 30:
            minute_text = 'half past'
        elif curr_time.minute > 30:
            if curr_time.minute == 45:
                minute_text = 'quarter to'
            else:
                minute_text = num2words(curr_time.minute) + ' minutes to'

        curr_hour = curr_time.hour
        if curr_time.minute > 30:
            curr_hour = curr_hour + 1

        if curr_hour == 24:
            curr_hour = 0

        if curr_hour == 0:
            hour_text = 'midnight'
        elif curr_hour < 12:
            hour_text = num2words(curr_hour) + ' am'
        elif curr_hour == 12:
            hour_text = 'noon'
        elif curr_hour > 12:
            hour_text = num2words(curr_hour-12) + ' pm'
        
        seconds_text = 'and ' + num2words(curr_time.second) + ' second'

        if curr_time.second > 1:
            seconds_text = seconds_text + 's'
        elif curr_time.second == 0:
            seconds_text = 'exactly'
            

        screen.blit(open_24_display_font.render('It is'.upper(),
                                                True,
                                                pi_clock.get_curr_clock_colour()),
                    (5, 110))
        screen.blit(open_24_display_font.render(minute_text.upper(),
                                                True,
                                                pi_clock.get_curr_clock_colour()),
                    (5, 140))

        screen.blit(open_24_display_font.render(hour_text.upper(),
                                                True,
                                                pi_clock.get_curr_clock_colour()),
                    (5, 170))

        screen.blit(open_24_display_font.render(seconds_text.upper(),
                                                True,
                                                pi_clock.get_curr_clock_colour()),
                    (5, 200))
        pygame.display.flip()
        clock.tick(clock_ticks)


if __name__ == '__main__':
    run_clock()
