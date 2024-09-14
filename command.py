from pathlib import Path
import re
import os
import importlib

commands: list[dict] = []

cmd_dir = "commands"
for dir_entry in os.scandir(cmd_dir):
    if dir_entry.is_file():
        path = Path(dir_entry.name)
        if path.suffix == ".py":
            stem = path.stem
            commands.append({
                "name": stem,
                "callback": importlib.import_module(f"{cmd_dir}.{stem}").callback
            })


def get_command(input: str):
    for command in commands:
        if input == command["name"]:
            return command["name"], None, command["callback"]
        args = re.findall(f"^{command["name"]}(.+)", input)
        if args:
            return command["name"], args, command["callback"]
    return None, None, None


def process_input(input):
    if input == "":
        return
    cmd, args, callback = get_command(input)
    if not cmd and not args:
        return
    callback(args)
