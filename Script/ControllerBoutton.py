
import time
class Controller:
    def __init__(self):
        self.is_playing = False
        self.is_paused = False
        self.is_resume = False
        self.is_stopped = False
    
    def play(self):
        if not self.is_resume:
            self.is_stopped = False
            self.is_playing = True
            self.start_time = time.time()
            self.current_time = time.time()
        else:
            self.is_stopped = False
            self.is_playing = True

    def pause(self):

        if self.is_playing:
            self.is_stopped = False
            self.is_playing = False
            self.is_paused = True
            self.pause_time = time.time()
            

    def stop(self):
        self.is_stopped = True
        self.is_playing = False
        self.milliemeseconde_show = 0
        self.heure = 0
        self.minute = 0
        self.seconde = 0


    def resume(self):
        if not self.is_playing and self.is_paused:
            self.is_resume = True
            self.is_paused = False
            self.is_playing = True
            self.play()
            self.pause_time = 0

    def plus(self):
        print("Plus")
