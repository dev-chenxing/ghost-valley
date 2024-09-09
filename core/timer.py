import time
from lib.zhongwen.number import 中文数字

game_time = None
real_time = None


class Time:
    def __init__(self, init_time=0) -> None:
        self.time = init_time

    def format(self):
        def get_season(month: int) -> str:
            match month:
                case m if 1 <= m <= 3:
                    return "春"
                case m if 4 <= m <= 6:
                    return "夏"
                case m if 7 <= m <= 9:
                    return "秋"
                case m if 10 <= m <= 12:
                    return "冬"
                case _:
                    return

        def get_mday(mday: int) -> str:
            match mday:
                case d if 1 <= d <= 9:
                    return f"初{中文数字(mday)}"
                case m if 10 <= m <= 30:
                    return f"{中文数字(mday)}日"
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
        tm = time.gmtime(self.time)
        t = time.struct_time((tm.tm_year - 1969, tm.tm_mon, tm.tm_mday, tm.tm_hour,
                              tm.tm_min, tm.tm_sec, tm.tm_wday, tm.tm_yday, tm.tm_isdst))
        era_name = "阎罗王"
        year = 中文数字(t.tm_year) if t.tm_year != 1 else "元"
        season = get_season(t.tm_mon)
        month = 中文数字(t.tm_mon) if t.tm_mon != 1 else "正"
        mday = get_mday(t.tm_mday)
        hour_period = get_hour_period(t.tm_hour)
        return f"{era_name}{year}年{season}{month}月{mday}，{hour_period}"


def game_time_thread():
    timescale = 360
    while True:
        time.sleep(1/timescale)
        game_time.time += 1


def real_time_thread():
    while True:
        time.sleep(1)
        real_time.time += 1
