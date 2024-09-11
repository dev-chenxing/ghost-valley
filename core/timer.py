import time
import datetime
import cnlunar
from lib.zhongwen.number import 中文数字

game_time = None
real_time = None


class Time:
    def __init__(self, init_time=0) -> None:
        self.time = init_time

    def format(self):
        def get_month(month: int) -> str:
            match month:
                case 1:
                    return "正月"
                case 12:
                    return "腊月"
                case _:
                    return f"{中文数字(month)}月"

        def get_day(day: int) -> str:
            match day:
                case d if 1 <= d <= 9:
                    return f"初{中文数字(day)}"
                case m if 10 <= m <= 30:
                    return f"{中文数字(day)}日"
                case _:
                    return

        def get_hour_period(hour: int) -> str:
            match hour:
                case 0:
                    return "深夜子时"
                case h if 1 <= h <= 2:
                    return "深夜丑时"
                case h if 3 <= h <= 4:
                    return "凌晨寅时"
                case h if 5 <= h <= 6:
                    return "凌晨卯时"
                case h if 7 <= h <= 8:
                    return "早晨辰时"
                case h if 9 <= h <= 10:
                    return "早晨巳时"
                case h if 11 <= h <= 12:
                    return "午间午时"
                case h if 13 <= h <= 14:
                    return "午间未时"
                case h if 15 <= h <= 16:
                    return "黄昏申时"
                case h if 17 <= h <= 18:
                    return "黄昏酉时"
                case h if 19 <= h <= 20:
                    return "夜晚戌时"
                case h if 21 <= h <= 22:
                    return "夜晚亥时"
                case 23:
                    return "深夜子时"
                case _:
                    return
        t = datetime.datetime.fromtimestamp(
            self.time, tz=datetime.timezone.utc)
        t_offset = datetime.datetime(
            t.year, t.month+1, t.day+5, t.hour, t.minute)
        lunar_t = cnlunar.Lunar(t_offset)

        era_name = "阎罗王"
        lunar_year = lunar_t.lunarYear - 1969
        year = 中文数字(lunar_year) if lunar_year != 1 else "元"
        season = lunar_t.lunarSeason
        month = get_month(lunar_t.lunarMonth)
        day = get_day(lunar_t.lunarDay)
        hour_period = get_hour_period(t.hour)
        return f"{era_name}{year}年{season}{month}{day}，{hour_period}"


def game_time_thread():
    timescale = 360
    while True:
        time.sleep(1)
        game_time.time += timescale


def real_time_thread():
    while True:
        time.sleep(1)
        real_time.time += 1
