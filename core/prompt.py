import time
import keyboard
from rich import print
from rich.console import Console

console = Console()


def prompt(text: str, default: str = None, suffix: str = "："):
    prefix = "> "
    default_text = f" [{default}]" if default else ""
    main_text = f"{text}\n"
    print(main_text)
    # result = console.input(f"{prefix}{main_text}{
    #                        default_text}{suffix}") or default
    result = console.input(prefix) or default
    print("")
    return result


def say(who: str = None, text: str = None):
    print(f"{text}\n")
    if keyboard.read_key(suppress=True):
        time.sleep(0.1)
        return
