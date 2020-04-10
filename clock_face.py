from datetime import datetime
import threading


class pi_clock_face:
    clock_mode = True
    clock_fade = 1
    timer = None


    def __init__(self):
        self.timer = threading.Timer(10.0, self.__switch_off_clock) 
        self.timer.start()

    def reset_clock(self):
        self.timer.cancel()
        self.clock_mode = True
        self.timer = threading.Timer(10.0, self.__switch_off_clock)
        self.timer.start()

    def __switch_off_clock(self):
        print('Switcing off clock')
        self.clock_mode = False
        self.clock_fade = 1

    def get_curr_clock_colour(self):
        if self.clock_mode:
            return (255,255,255)
        else:
            clock_colour = (255*self.clock_fade,255*self.clock_fade,255*self.clock_fade)
            self.clock_fade = self.clock_fade - 0.01
            if self.clock_fade < 0:
                self.clock_fade = 0
            return clock_colour
