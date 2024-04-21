import time
import os
from Script.ControllerBoutton import Controller


class Module(Controller):
    def __init__(self):
        super().__init__()
        self.super = super()
        self.start_time = 0
        self.pause_time = 0
        self.current_time = 0
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.milliemeseconde_show = 0

    def count_digits(self, number):
        return sum(c.isdigit() for c in str(number))

    def time_counter(self):
        self.current_time = time.time()

        if self.is_playing and not self.is_paused:
            time.sleep(0.095)
            if not self.is_resume:
                milliseconds = int(
                    (self.current_time - self.start_time) * 1000)
                self.milliemeseconde_show = milliseconds

            elif self.is_resume:
                self.start_time = self.current_time - \
                    (int(self.milliemeseconde_show) / 1000)
                milliseconds = int(
                    (self.current_time - self.start_time) * 1000)
            else:
                milliseconds = 0
            self.is_resume = False
            milliemeseconde_show, second_show, minute_show, hours_show = self.ConvertionAffichage(
                milliseconds)

            return (milliemeseconde_show, second_show, minute_show, hours_show)

        elif self.is_paused and not self.is_stopped:
            milliseconds = int((self.pause_time - self.start_time) * 1000)
            milliemeseconde_show, second_show, minute_show, hours_show = self.ConvertionAffichage(
                milliseconds)
            return (milliemeseconde_show, second_show, minute_show, hours_show)

        elif self.is_stopped:
            return "00", "00", "00", "00"
        else:
            return "00", "00", "00", "00"

    def ConvertionAffichage(self, milliseconds):
        self.milliemeseconde_show = milliseconds
        if (890 < milliseconds):
            self.start_time = time.time()
            milliseconds = 0
            self.seconde += 1

        if (self.seconde == 60):
            self.seconde = 0
            self.minute += 1

        if (self.minute == 60):
            self.minute = 0
            self.heure += 1

        nb_minute = self.count_digits(self.minute)
        nb_heure = self.count_digits(self.heure)
        nb_seconde = self.count_digits(self.seconde)
        nb_tierce = self.count_digits(self.milliemeseconde_show)

        if (nb_tierce == 2):
            milliemeseconde_show = f"0{self.milliemeseconde_show}"
        elif (nb_tierce == 1):
            milliemeseconde_show = f"00{self.milliemeseconde_show}"
        else:
            milliemeseconde_show = f"{self.milliemeseconde_show}"

        if (nb_seconde == 1):
            second_show = f"0{self.seconde}"
        else:
            second_show = f"{self.seconde}"

        if (nb_minute == 1):
            minute_show = f"0{self.minute}"
        else:
            minute_show = f"{self.minute}"

        if (nb_heure == 1):
            hours_show = f"0{self.heure}"
        else:
            hours_show = f"{self.heure}"

        return (milliemeseconde_show, second_show, minute_show, hours_show)


if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(parent_dir, ".."))
    os.system("python main.py")
