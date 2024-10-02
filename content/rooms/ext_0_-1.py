from core.prompt import say, select, idle_talk
from core.room import Room
import game
from utils import i18n

id = "归云派山脚"
name = "归云派山脚"
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
    if 突遭变故 == 1:
        idle_talk(who="陈远舟", text="跑到这里应该就安全了吧。")
        idle_talk(who="陈远舟", text="各位没有受伤吧？")
        idle_talk(who="卫泓", text="人是没事，就是吓得半死。")
        idle_talk(who="纪瑶华", text="那道奇异的光……似乎是有高人相助我们才得以逃脱。")
        # select(who="纪瑶华", text="不过方才有一人逆行冲上去了，他不会有事吧？",
        #        choices=["把杨子勤的话告诉众人。"])
        # say(who="陈远舟", text="此等危急时刻弃之而去实在太不道义，我去帮他们。")
        # say(who="卫泓", text="我也去。")
        # say(who="纪瑶华", text="救人要紧，你快去找大夫吧。")


def can_change_room(room_to: Room = None, room_from: Room = None):
    if room_to.id == "归云派山门":
        突遭变故 = game.get_quest_stage(id="突遭变故")
        if 突遭变故 < 2:
            say(who="杨子勤", text="姑娘请留步，此刻山顶情况凶险难料，万不可以以身犯险。")
        elif 突遭变故 == 2:
            say(text="此刻山顶情况凶险难料，还是不要上去了。")
        return False
    return True
