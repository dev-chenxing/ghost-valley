import threading
from rich import print


from command import process_input
from lib.zhongwen.number import 中文数字
import game
from core.player import Player
from core import timer
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

    farm = game.create_room(id="farm")
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
    # print("[bold wheat1]创建角色[/bold wheat1]")
    # game.player.name = prompt(
    #     "请输入你的自称", default=f"[wheat1]{game.player.name}[/wheat1]", same_line=True, bold=True)
    # game.player.female = prompt("请选择你的性别", show_choices=True, choices=[
    #                             "男", "女"], same_line=True, bold=True) == "女"
    # say(who=game.player.name, text=f"小的叫{game.player.name}")

    white_radish = game.create_object(objectType="crop", id="white_radish")
    white_radish.name = "白萝卜"
    white_radish_seed = game.create_object(
        objectType="seed", id="white_radish_seed")
    white_radish_seed.name = "白萝卜种子"
    white_radish_seed.crop = "white_radish"
    carrot = game.create_object(objectType="crop", id="carrot")
    carrot.name = "胡萝卜"
    carrot_seed = game.create_object(objectType="seed", id="carrot_seed")
    carrot_seed.name = "胡萝卜种子"
    carrot_seed.crop = "carrot"
    game.add_item(item=white_radish_seed, count=15)
    game.add_item(item=carrot_seed)

    game.save_game()

    game_time_thread.start()
    real_time_thread.start()

    while running:
        cmd = input("> ")
        process_input(cmd)

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
