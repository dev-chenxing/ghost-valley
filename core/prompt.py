from typing import Union
import click
from rich import print
from rich.console import Console
from rich.spinner import Spinner
import time
from InquirerPy import inquirer, get_style
from InquirerPy.base.control import Choice
from InquirerPy.utils import color_print

from lib import palette

console = Console()


def prompt(text: str, default: str = None, suffix: str = "：", show_choices: bool = False, choices: list[str] = None, invalid_text: str = "...", same_line: bool = False, bold: bool = False):
    prefix = "> "
    choices_text = f" [{
        "/".join(choices)}]" if show_choices and choices else ""
    default_text = f" [{default}]" if default else ""
    text = f"[bold grey85]{text}[/bold grey85]" if bold else text
    if same_line:
        while True:
            result = console.input(f"{prefix}{text}{choices_text}{default_text}{
                suffix}") or default
            if result and (not choices or result in choices):
                return result
            else:
                print(invalid_text)
    else:
        print(f"{text}")
        while True:
            result = console.input(prefix) or default
            if result in choices:
                return result
            else:
                print(invalid_text)


def get_character_color(id: str, mode: str = "name") -> str:
    color = "light_goldenrod2"
    if mode == "name":
        return color
    elif mode == "hex":
        return palette.get(color)["hex"]


def say(who: str = None, action: str = "", text: str = None, hint: bool = False, no_quotation: bool = False):
    color = get_character_color(who)
    who_text = f"[{color}]{who}[/{color}]" if who else ""
    main_text = text
    if who:
        if not no_quotation:
            main_text = f"“{text}”"
        main_text = f"：{text}"
    hint_text = "[bright_black]请按回车键继续[/bright_black]" if hint else ""
    print(f"{who_text}{action}{main_text}{hint_text}", end="")
    try:
        click.prompt(text="", prompt_suffix="", default="",
                     show_default=False, hide_input=True)
    except (click.exceptions.Abort):
        exit(0)


def select(choices: Union[list[dict], list[str]], text: str = None, default: str = None, suffix: str = ":", who: str = None) -> str:
    who_color = get_character_color(who, mode="hex")
    who_text = f"{who}:" if who else ""
    suffix = "" if who else suffix
    qmark = "> " if text else ""
    qmark = who_text if who else qmark
    amark = qmark
    main_text = f"{text}{suffix}" if text else ""
    main_text = f"“{main_text}”" if who else main_text
    choice_list = [Choice(name=choice, value=i) if isinstance(choice, str) else Choice(name=choice["name"], value=choice["value"])
                   for i, choice in enumerate(choices)]
    return inquirer.select(
        message=main_text,
        choices=choice_list,
        default=default,
        qmark=qmark,
        amark=amark,
        pointer="🌱",
        show_cursor=False,
        transformer=None if text else lambda _: "",
        style=get_style(
            {"pointer": "#AFD75F", "question": "" if who else "bold", "answered_question": "" if who else "bold", "answer": "#AFD75F", "questionmark": who_color, "answermark": who_color})
    ).execute()


def spinner(text: str, seconds: float = 3):
    with console.status(text):
        time.sleep(seconds)
