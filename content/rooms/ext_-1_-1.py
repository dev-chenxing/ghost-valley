from core.prompt import say, select, spinner
import game
from utils import i18n

id = "回春堂"
name = "回春堂"
grid_x = -1
grid_y = -1


def callback():
    突遭变故 = game.get_quest_stage(id="突遭变故")
    if 突遭变故 == 1:
        say(who="孙大夫", text="这动静可真不小啊……难道是归云派发生了什么变故？")
        select(who="孙大夫", text=f"嗯？小{
            "姑娘" if game.player.female else "伙子"}神色匆匆，找我有何事？", choices=["向孙大夫说明情况。"])
        say(who="孙大夫", text="救人要紧。我收拾下药箱就去客栈！")
        spinner(seconds=1)
        say(text="也不知那位归云弟子情况如何，快去客栈看看吧。")
        game.update_quest(id="突遭变故", stage=2)
