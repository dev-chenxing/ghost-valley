import time
from utils import format_time

game_time: int = None
real_time: int = None


class Time:
    def __init__(self, init_time=0) -> None:
        self.time = init_time

    def format(self):
        return format_time(self.time)


def game_time_thread():
    timescale = 360
    while True:
        time.sleep(1)
        game_time.time += timescale


def real_time_thread():
    while True:
        time.sleep(1)
        real_time.time += 1
