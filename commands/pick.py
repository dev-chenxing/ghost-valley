from rich import print
import game
from lib.chinese_number import 中文数字

name = "捡"


def callback(args: list[str]):
    item = game.get_object(name=args[0])
    count = 1
    game.add_item(item=item, count=count)
    print(f"从地上捡起了{中文数字(count, 两=True)}{
          item.unit}[{item.color}]{item.name}[/{item.color}]")
