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
    print("[bold]归云派[/bold]")
    select(who="归云派弟子", message="这位道友留步，不知来我归云派所为何事？",
           choices=["将左长老的信物交给他查看。"])
