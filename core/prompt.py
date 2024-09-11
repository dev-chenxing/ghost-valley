import time
import click
import keyboard
from rich import print
from rich.console import Console

console = Console()


def prompt(text: str, default: str = None, suffix: str = "：", show_choices: bool = False, choices: list[str] = None, invalid_text: str = "...", same_line: bool = False, bold: bool = False):
    prefix = "> "
    choices_text = f" [{
        "/".join(choices)}]" if show_choices and choices else ""
    default_text = f" [{default}]" if default else ""
    text = f"[bold grey85]{text}[/bold grey85]" if bold else text
    if same_line:
        if choices:
            while True:
                result = console.input(f"{prefix}{text}{choices_text}{default_text}{
                    suffix}") or default
                if result in choices:
                    return result
                else:
                    print(invalid_text)
        else:
            return console.input(f"{prefix}{text}{choices_text}{default_text}{
                suffix}") or default
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
