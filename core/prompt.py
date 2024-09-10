import rich
from rich.console import Console

console = Console()


def prompt(text: str, default: str = None):
    prefix = ">"
    suffix = "："
    return console.input(f"{prefix} [bold]{text}[/bold] [{default}]{suffix}") or default
