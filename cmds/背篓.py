from rich import print
import game


def callback(args: list[str]):
    item_stack_strings: list[str] = []
    for item_stack in game.player.inventory:
        color = item_stack.object.color
        item_stack_strings.append(
            f"[{color}]{item_stack.to_string()}[/{color}]")
    print(f"背篓里放了{"，".join(item_stack_strings)}")
