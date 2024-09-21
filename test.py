import sys
import threading
import time
from os import system
system("")


def screen_output():
    msg = "something"
    while True:
        with threading.Lock():
            print("\x1b[s\x1b[1A\x1b[999D\x1b[1S\x1b[L" +
                  msg+"\x1b[u", end="", flush=True)
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
