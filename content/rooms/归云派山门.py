from core.prompt import say, select
import game


grid_x = 0
grid_y = 0


def callback():
    # select(who="归云派弟子", text="这位道友留步，不知来我归云派所为何事？",
    #        choices=["将左长老的信物交给他查看。"])
    # say(who="归云派弟子", text=f"原来你就是{game.player.name}？太好了，左长老命我前来接引。我已在此恭候多时了。")
    # say(who="归云派弟子", text="说起来那山岚谷也是丰饶富庶之地。只可惜我派剑修当道，灵植一道无甚人才，这才让它荒废至今。")
    # select(who="归云派弟子", text="此刻左长老正在主峰议事。长老他让我将这山岚谷禁制的符咒先交给你，晚点他会亲自带你过去。",
    #        choices=["前面似乎聚了很多人，可是发生了什么事？"])
    # say(who="归云派弟子", text="哦，归云派最近正在招募新弟子，他们都是前来参加入门考核的散修。")
    # say(who="归云派弟子", text="我派考核向来严格，能入选者不过十之一二。不过道友是左长老亲自选定之人，自然不必参加考核。")
    # say(who="归云派弟子", text="还请道友先随他们一起在大殿前等候片刻。我这就去通禀一声。")
    # print("")
    # say(text="使用命令[东][南][西][北]可操作角色行走")
    # say(text="向[bold]北[/bold]走前往[bold]大殿[/bold]，和其他人一起等候通禀吧。")
    print("")
    game.update_quest(id="初入归云", stage=1)


def can_change_room():
    if game.get_quest("初入归云").finished:
        return True
    else:
        print("现在不是闲逛的时候，先去殿前等候吧。")
