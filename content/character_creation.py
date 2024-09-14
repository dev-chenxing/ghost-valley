from rich import print
from core.prompt import prompt, say
import game


def character_creation():
    print("[bold wheat1]创建角色[/bold wheat1]")
    game.player.name = prompt(
        "请输入你的自称", default=f"[wheat1]{game.player.name}[/wheat1]", same_line=True, bold=True)
    # game.player.female = prompt("请选择你的性别", show_choices=True, choices=[
    #     "男", "女"], same_line=True, bold=True) == "女"
