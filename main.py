import threading
from rich import print


from lib.zhongwen.number import 中文数字
from core import timer
from core.prompt import say, prompt
import game
from core.player import Object, Player, get_item_color, get_item_count, get_object, plant, set_attributes
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

    game.player = Player()
    # say(text="你再次醒来时，环顾四周，虽然此刻天色漆黑，借着月光不难看出自己身处一片幽林中的小径旁。")
    # say(text="这个没有指示牌的[wheat1]鬼地方[/wheat1]。")
    # direction = prompt(
    #     "要沿着小径而[bold green]上山[/bold green]吗？还是沿着小径[bold green]下山[/bold green]？", suffix="", choices=["上山", "下山"], invalid_text="你要往哪里走？")
    # if direction == "上山":
    #     say(text="你循着[bold green]小径而上[/bold green]，走了不知多少时辰。")
    #     say(
    #         text="正因为四周尽是树木，所以当目光与迎面飘来的那抹[bold dark_red]红色身影[/bold dark_red]撞上时，你吓得僵在原地，不敢动弹。")
    #     say(text="那是个[dark_red]女鬼[/dark_red]，脸色煞白，身着红衫。")
    #     say(text="眼看着女鬼离自己越来越近，正当以为自己小命不保时————")
    #     say(who="女鬼", action="问道", text="小鬼，你唤做甚么？")
    #     say(text="没有想象中的鬼哭狼嚎，女鬼声音轻柔舒缓，且这话问得突然，你一愣，半天没有反应过来。")
    print("[bold wheat1]创建角色[/bold wheat1]")
    game.player.name = prompt(
        "请输入你的自称", default=f"[wheat1]{game.player.name}[/wheat1]", same_line=True, bold=True)
    game.player.female = prompt("请选择你的性别", show_choices=True, choices=[
                                "男", "女"], same_line=True, bold=True) == "女"
    say(who=game.player.name, text=f"小的叫{game.player.name}")

    game_time_thread.start()
    real_time_thread.start()
    while running:
        cmd = input("> ")
        if cmd == "时间":
            print(f"现在 游戏 时间是：[bright_yellow]{
                timer.game_time.format()}[/bright_yellow]")
        elif cmd == "荷包":
            print(f"{game.player.name}摸了摸自己荷包里的[light_goldenrod1]{
                  中文数字(game.player.coins)}文钱[/light_goldenrod1]")
        elif cmd == "背篓":
            item_stack_strings = []
            for item_stack in game.player.inventory:
                color = get_item_color(item_stack.object)
                item_stack_strings.append(
                    f"[{color}]{item_stack.to_string()}[/{color}]")
            print(f"背篓里放了{"，".join(item_stack_strings)}")
        elif cmd == "种下全部白萝卜种子":
            item = get_object("white_radish_seeds")
            for _ in range(get_item_count(item)):
                plant(seeds=item)
        elif cmd == "田":
            if not game.field:
                print("田里还荒着，没种东西")
            else:
                plant_strings = []
                plants: dict[Object, int] = {}
                for ref in game.field:
                    if ref.object not in plants:
                        plants[ref.object] = 1
                    else:
                        plants[ref.object] += 1
                for plant, count in plants.items():
                    color = get_item_color(plant)
                    plant_strings.append(
                        f"[{color}]{中文数字(count, 两=True)}{plant.unit}{plant.name}[/{color}]")
                print(f"田里种着{"，".join(plant_strings)}")

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
