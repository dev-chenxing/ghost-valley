import math
from rich import print
import time

from lib.zhongwen.number import 中文数字


timestamp_start = time.time()
timestamp = 0
timescale = 20000
game_time: time.struct_time


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
            return "夜半子时"
        case h if 1 <= h <= 2:
            return "鸡鸣丑时"
        case h if 3 <= h <= 4:
            return "平旦寅时"
        case h if 5 <= h <= 6:
            return "日出卯时"
        case h if 7 <= h <= 8:
            return "早食辰时"
        case h if 9 <= h <= 10:
            return "禺中巳时"
        case h if 11 <= h <= 12:
            return "日中午时"
        case h if 13 <= h <= 14:
            return "日昳未时"
        case h if 15 <= h <= 16:
            return "晡时申时"
        case h if 17 <= h <= 18:
            return "日入酉时"
        case h if 19 <= h <= 20:
            return "黄昏戌时"
        case h if 21 <= h <= 22:
            return "人定亥时"
        case 23:
            return "夜半子时"
        case _:
            return


def time_description(t: time.struct_time) -> str:
    era_name = "阎罗王"
    year = 中文数字(t.tm_year) if t.tm_year != 1 else "元"
    season = get_season(t.tm_mon)
    month = 中文数字(t.tm_mon) if t.tm_mon != 1 else "正"
    mday = get_mday(t.tm_mday)
    hour_period = get_hour_period(t.tm_hour)
    return f"{era_name}{year}年{season}{month}月{mday}，{hour_period}"


def game_time_description() -> str:
    global game_time
    return time_description(game_time)


def to_game_time(t: float) -> time.struct_time:
    tm = time.gmtime(t)
    return time.struct_time((tm.tm_year - 1969, tm.tm_mon, tm.tm_mday, tm.tm_hour,
                            tm.tm_min, tm.tm_sec, tm.tm_wday, tm.tm_yday, tm.tm_isdst))


def main():
    while True:
        global timestamp, timestamp_start, game_time
        timestamp = (time.time() - timestamp_start) * timescale
        game_time = to_game_time(timestamp)
        print(f"现在 游戏 时间是：[bright_yellow]{
            game_time_description()}[/bright_yellow]")
