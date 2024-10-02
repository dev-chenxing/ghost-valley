import importlib
from inspect import isfunction
import json
import os
from pathlib import Path
import datetime
import cnlunar
import bisect

from lib.chinese_number import 中文数字
import settings


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


def format_time(seconds: int, style: str = "long"):
    t = datetime.datetime.fromtimestamp(
        seconds, tz=datetime.timezone.utc)
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

    if style == "short":
        return f"{year}年{season}{month}{day}"
    else:
        return f"{era_name}{year}年{season}{month}{day}，{hour_period}"


def get_saves() -> list:
    saves = []
    saves_dir = "saves"
    if not os.path.isdir(saves_dir):
        os.makedirs(saves_dir)
    for dir_entry in os.scandir(saves_dir):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".json":
                with open(os.path.join(saves_dir, dir_entry.name), encoding='utf8') as save_file:
                    data = json.load(save_file)
                    name = f"{data["player"]["name"]} {
                        format_time(data["game_time"], style="short")}"
                    bisect.insort(saves, {"value": path.stem, "name": name,
                                  "timestamp": data["timestamp"]}, key=lambda save: save["timestamp"])
    saves = [{"value": save["value"], "name": f"{index+1}. {save["name"]}"}
             for index, save in enumerate(saves)]
    return saves


def save_file_exists():
    saves = get_saves()
    if saves == []:
        return False
    else:
        return True


def get_languages() -> list:
    languages = []
    i18n_dir = "i18n"
    for dir_entry in os.scandir(i18n_dir):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".py":
                translation = importlib.import_module(f"i18n.{path.stem}")
                languages.append(
                    {"value": path.stem, "name": translation.language_name})
    return languages


def i18n(attr: str, **kwargs):
    translation_module = importlib.import_module(f"i18n.{settings.language}")
    if hasattr(translation_module, attr):
        translation = getattr(translation_module, attr)
    else:
        translation_module = importlib.import_module(
            f"i18n.{settings.default_language}")
        translation = getattr(translation_module, attr)
    if isfunction(translation):
        return translation(**kwargs)
    else:
        return translation
