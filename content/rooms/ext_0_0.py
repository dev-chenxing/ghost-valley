from core.prompt import say, select
from core.room import Room
import game
from utils import i18n

id = "归云派山门"
name = "归云派山门"
grid_x = 0
grid_y = 0


def callback():
    select(who="归云派弟子", text=i18n("归云派弟子_01"),
           choices=[i18n("归云派弟子_01_01")])
    say(who="归云派弟子", text=i18n("归云派弟子_02"))
    say(who="归云派弟子", text=i18n("归云派弟子_03"))
    select(who="归云派弟子", text=i18n("归云派弟子_04"),
           choices=[i18n("归云派弟子_04_01")])
    say(who="归云派弟子", text=i18n("归云派弟子_05"))
    say(who="归云派弟子", text=i18n("归云派弟子_06"))
    say(who="归云派弟子", text=i18n("归云派弟子_07"))
    print("")
    say(text=i18n("归云派山门_01"))
    say(text=i18n("归云派山门_02"))
    print("")
    game.update_quest(id="初入归云", stage=1)


def can_change_room(room_to: Room = None, room_from: Room = None):
    if room_to.id != "归云派大殿":
        if not game.get_quest("初入归云").finished:
            print(i18n("归云派山门_03"))
            return False
    return True
