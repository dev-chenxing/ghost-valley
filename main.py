import threading
from rich import print


from lib.zhongwen.number import 中文数字
from core import timer
from core.prompt import say, prompt
from core.player import Object, Player, Reference, get_item_color
from help.title import title


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
    say(text="你再次醒来时，环顾四周，虽然此刻天色漆黑，借着月光不难看出自己身处一片幽林中的小径旁。")
    say(text="这个没有指示牌的[wheat1]鬼地方[/wheat1]。")
    direction = prompt(
        "要沿着小径而[bold red]上山[/bold red]吗？还是沿着小径[bold red]下山[/bold red]？", suffix="")
    if direction == "上山":
        say("你循着[bold red]小径而上[/bold red]，走了不知多少时辰。")
        say("正因为四周尽是树木，所以当目光与迎面飘来的那抹红色身影撞上时，你吓得僵在原地，不敢动弹。")
        say("那是个[dark_red]女鬼[/dark_red]，脸色煞白，身着红衫。")
        say("眼看着女鬼离自己越来越近，正当以为自己小命不保时，女鬼问道：“小鬼你唤做甚么？”")
        say("没有想象中的鬼哭狼嚎，女鬼声音轻柔舒缓，且这话问得突然，你一愣，半天没有反应过来。")
        player.name = prompt("自称", default=f"[wheat1]{player.name}[/wheat1]")
        say(f"{player.name}：“小的叫{player.name}”")

    field: list[Reference] = []

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
            item_stack_strings = []
            for item_stack in player.inventory:
                color = get_item_color(item_stack.object)
                item_stack_strings.append(
                    f"[{color}]{item_stack.to_string()}[/{color}]")
            print(f"背筐里放了{"，".join(item_stack_strings)}")
        elif cmd == "种下全部白萝卜种子":
            pass
        elif cmd == "田":
            if not field:
                print("田里还荒着，没种东西")
            else:
                plant_strings = []
                plants: dict[Object, int] = {}
                for ref in field:
                    if ref.object not in plants:
                        plants[ref.object] = 1
                    else:
                        plants[ref.object] += 1
                for plant, count in plants.items():
                    color = get_item_color(plant)
                    plant_strings.append(
                        f"[{color}]{中文数字(count)}{plant.unit}{plant.name}[/{color}]")
                print(f"田里种着{"，".join(plant_strings)}")

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
