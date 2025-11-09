import inspect
from pyrogram.types import BotCommand
from .bot_commands import BotCommands

async def set_bot_commands(client):
    commands = []
    for _, obj in inspect.getmembers(BotCommands):
        if isinstance(obj, list):
            for cmd in obj:
                commands.append(BotCommand(cmd.split()[0], f"/{cmd}"))
        elif isinstance(obj, str):
            commands.append(BotCommand(obj.split()[0], f"/{obj}"))

    await client.set_bot_commands(commands)
