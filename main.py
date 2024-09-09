import threading
from rich import print


from core import timer
from core.player import Player, get_item_color
# from help.welcome import welcome
from help.title import title
from lib.zhongwen.number import 中文数字
# from cmds import time

print(title)

timer.game_time = timer.Time()
timer.real_time = timer.Time()

try:

    running = True

    game_time_thread = threading.Thread(
        target=timer.game_time_thread, daemon=True)
    real_time_thread = threading.Thread(
        target=timer.real_time_thread, daemon=True)

    player = Player()

    game_time_thread.start()
    real_time_thread.start()

    while running:
        cmd = input("> ")
        if cmd == "时间":
            print(f"现在 游戏 时间是：[bright_yellow]{
                timer.game_time.format()}[/bright_yellow]")
        elif cmd == "荷包":
            print(f"{player.name}摸了摸自己荷包里的[light_goldenrod1]{
                  中文数字(player.coins)}文钱[/light_goldenrod1]")
        elif cmd == "背筐":
            inventory_strings = []
            for item_stack in player.inventory:
                color = get_item_color(item_stack.object)
                inventory_strings.append(
                    f"[{color}]{item_stack.to_string()}[/{color}]")
            print(f"背筐里放了{"，".join(inventory_strings)}")

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
