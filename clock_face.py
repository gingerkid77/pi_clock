from datetime import datetime
import threading

from num2words import num2words
from pygame import Surface
from pygame import font


class pi_clock_face:
    clock_mode = True
    clock_fade = 1
    timer = None
    fade_speed = 100
    enable_fade = False
    clock_surface: Surface = None
    display_font: font

    def __init__(self,clock_surface: Surface,fade_speed=100,enable_fade=False):
        self.fade_speed = fade_speed
        self.enable_fade = enable_fade
        self.clock_surface = clock_surface
        self.display_font = font.Font('CamingoCode-Regular.ttf', 16)

    def start_fade(self):
        if self.enable_fade:
            self.timer = threading.Timer(10.0, self.__switch_off_clock) 
            self.timer.start()

    def reset_clock(self):
        self.timer.cancel()
        self.clock_mode = True
        self.start_fade()

    def kill_clock(self):
        if self.timer is not None:
            self.timer.cancel()

    def __switch_off_clock(self):
        self.clock_mode = False
        self.clock_fade = 1

    def draw_clock(self):
        # Might want to think about handling dynamic Surface sizes at some point. Assuming pitft size for now

        curr_time = datetime.now()

        self.clock_surface.fill((0, 0, 0))

        self.clock_surface.set_colorkey((0,0,0))

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
            hour_text = num2words(curr_hour) + ' in the morning'
        elif curr_hour == 12:
            hour_text = 'noon'
        elif curr_hour > 12:
            hour_text = num2words(curr_hour - 12) + ' in the afternoon'

        seconds_text = 'and ' + num2words(curr_time.second) + ' second'

        if curr_time.second > 1:
            seconds_text = seconds_text + 's'
        elif curr_time.second == 0:
            seconds_text = 'exactly'

        self.clock_surface.blit(self.display_font.render('It is'.upper(),
                                                True,
                                                self.get_curr_clock_colour()),
                    (5, 110))
        self.clock_surface.blit(self.display_font.render(minute_text.upper(),
                                                True,
                                                self.get_curr_clock_colour()),
                    (5, 140))

        self.clock_surface.blit(self.display_font.render(hour_text.upper(),
                                                True,
                                                self.get_curr_clock_colour()),
                    (5, 170))

        self.clock_surface.blit(self.display_font.render(seconds_text.upper(),
                                                True,
                                                self.get_curr_clock_colour()),
                    (5, 200))

        return self.clock_surface

    def get_curr_clock_colour(self):
        if self.clock_mode:
            return (255,255,255)
        else:
            clock_colour = (255*self.clock_fade,255*self.clock_fade,255*self.clock_fade)
            self.clock_fade = self.clock_fade - (1/self.fade_speed)
            if self.clock_fade < 0:
                self.clock_fade = 0
            return clock_colour
