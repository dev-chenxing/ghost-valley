from rich import print
from core.prompt import prompt, select, spinner, say
import game


def cutscene():
    # spinner(text="载入中...", seconds=1)
    # print("")
    # say(text=f"{game.player.name}小友，\n    别来无恙？数月前于山中偶遇，相谈甚欢。我观小友于灵植一道颇有天赋，且有向道修行之心。如今正有一桩机缘送于小友：我归云派门下产业众多，其中一处山谷，名曰「山岚谷」，虽灵气丰沛，山清水秀，但苦于门中无人擅长耕作，以至荒废许久。", hint=True)
    # say(text="    前几日门中长老议事，正巧有人提议招募灵植散修如我归云派，专门打理山岚谷，并以此间产出的灵植草药向门派换取功法丹药，助其修行。此议正合小友所需，不知小友意下如何？")
    # say(text="    若小友有意，可凭此信来归云派寻我详谈。")
    # say(text="    归云派炼丹长老 左明渊")
    # spinner(text="载入中...", seconds=1)
    # print("")
    game.create_room(id="归云派山门")
    game.position_room("归云派山门")
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
    say(text="使用命令[东][南][西][北]可操作角色行走")
    say(text="向[bold]北[/bold]走前往[bold]大殿[/bold]，和其他人一起等候通禀吧。")
    game.create_quest(id="初入归云", stages={
        1: "向北走前往大殿处等候"
    })
    print("")
    game.update_quest(id="初入归云", stage=1)
