import time
import click
import keyboard
from rich import print
from rich.console import Console

console = Console()


def prompt(text: str, default: str = None, suffix: str = "：", choices: list[str] = None, invalid_text: str = "...", same_line: bool = False):
    prefix = "> "
    default_text = f" [{default}]" if default else ""
    if same_line:
        result = console.input(f"{prefix}{text}{default_text}{
                               suffix}") or default
        return result
    else:
        print(f"{text}")
        while True:
            result = console.input(prefix) or default
            if result in choices:
                return result
            else:
                print(invalid_text)


def get_character_color(id: str) -> str:
    return "dark_red"


def say(who: str = None, action: str = "", text: str = None):
    color = get_character_color(who)
    who_text = f"[{color}]{who}[/{color}]" if who else ""
    main_text = f"：“{text}”" if who else text
    print(f"{who_text}{action}{main_text}", end="")
    try:
        click.prompt(text="", prompt_suffix="", default="",
                     show_default=False, hide_input=True)
    except (click.exceptions.Abort):
        exit(0)
