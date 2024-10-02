from rich import print
from core.prompt import prompt, select, spinner, say
import game
from utils import i18n


def cutscene():
    spinner(text=f"{i18n("loading")}...", seconds=1)
    print("")
    say(text=i18n("intro_cutscene_01"), hint=True)
    say(text=i18n("intro_cutscene_02"))
    say(text=i18n("intro_cutscene_03"))
    say(text=i18n("intro_cutscene_04"))
    game.position_room("归云派山门")
