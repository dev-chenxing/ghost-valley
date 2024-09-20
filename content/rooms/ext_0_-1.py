from core.prompt import say, select
from core.room import Room
import game
from utils import save_file_exists

id = "归云派山下"
grid_x = 0
grid_y = -1


def callback():
    突遭变故 = game.get_quest_stage(id="突遭变故")
    if 突遭变故 < 1:
        say(who="杨子勤", text="这……这是怎么回事？")
        say(who="杨子勤", text="谢师兄？！你怎么了谢师兄？出什么事了？")
        say(who="杨子勤", text="谢师兄，谢师兄……？！")
        say(who="谢文天", text="……")
        say(who="杨子勤", text="（不能慌！这个时候千万不能慌，让我想想该怎么办……）", no_quotation=True)
        say(who="杨子勤", text="（……嗯，就这样！）", no_quotation=True)
        select(who="杨子勤", text="在下杨子勤。眼下救人要紧，还请道友帮忙跑一趟，去请大夫！",
               choices=["理当如此！"])
        say(who="杨子勤", text="镇上的孙大夫就住在西边的回春堂里。")
        say(who="杨子勤", text="我会先把谢师兄送到落霞客栈。")
        say(who="杨子勤", text="麻烦你请孙大夫尽快赶去救人！")
        game.update_quest(id="突遭变故", stage=1)
        answer = select(text="是否要存储游戏", choices=["是", "否"], suffix="？")
        if answer == 0:
            game.save_game(file=game.player.name)


def can_change_room(room_to: Room = None, room_from: Room = None):
    if room_to.id == "归云派山门":
        print("上山的路已被落石堵得严严实实")
        return False
    return True
