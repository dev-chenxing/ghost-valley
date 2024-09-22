import sys
import threading
import time
from rich import print as rprint
from rich.text import Text


def screen_output():
    who = "hello"
    text = "world"
    while True:
        with threading.Lock():
            # rprint(Text("\x1b[s\x1b[1A\x1b[999D\x1b[1S\x1b[L" + "[red]" +
            #             who + "[/red]" + text + "\x1b[u"), end="", flush=True)
            rprint(Text("\x1b[s\x1b[1A\x1b[999D\x1b[1S\x1b[L"), end="")
            rprint(Text(who+": ", style="light_goldenrod2"), end="")
            rprint(Text(text + "\x1b[u"), end="", flush=True)
            time.sleep(2)


def user_input():
    while True:
        some_input = input("type in something: ")
        print(f"you typed: {some_input}")


t1 = threading.Thread(target=screen_output, daemon=True)
t2 = threading.Thread(target=user_input, daemon=True)

t1.start()
t2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    sys.exit(1)
