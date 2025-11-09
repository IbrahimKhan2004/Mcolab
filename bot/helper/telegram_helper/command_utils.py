import inspect
from pyrogram.types import BotCommand
from .bot_commands import BotCommands
from ...core.config_manager import Config

COMMAND_DESCRIPTIONS = {
    'StartCommand': "Starts the bot",
    'MirrorCommand': "Mirror",
    'YtdlCommand': "Mirror yt-dlp supported links",
    'LeechCommand': "Upload to telegram",
    'YtdlLeechCommand': "Leech yt-dlp supported links",
    'CloneCommand': "Copy file/folder to Drive",
    'CountCommand': "Count file/folder from GDrive",
    'DeleteCommand': "Delete file/folder from GDrive",
    'CancelTaskCommand': "Cancel a task",
    'CancelAllCommand': "Cancel all tasks",
    'ForceStartCommand': "Start task from queue",
    'ListCommand': "Search files in Drive",
    'StatusCommand': "Get Mirror Status message",
    'UsersCommand': "Show users settings",
    'AuthorizeCommand': "Authorize user or chat",
    'UnAuthorizeCommand': "Unauthorize user or chat",
    'AddSudoCommand': "Add sudo user",
    'RmSudoCommand': "Remove sudo user",
    'PingCommand': "Ping the Bot",
    'RestartCommand': "Restart the Bot",
    'RestartSessionsCommand': "Restart Telegram Session(s)",
    'StatsCommand': "Bot Usage Stats",
    'HelpCommand': "All cmds with description",
    'LogCommand': "Get the Bot Log",
    'ShellCommand': "Run commands in Shell",
    'AExecCommand': "Execute async function",
    'ExecCommand': "Execute sync function",
    'ClearLocalsCommand': "Clear exec locals",
    'BotSetCommand': "Bot settings",
    'UserSetCommand': "User settings",
    'SelectCommand': "Select files from torrent",
    'RssCommand': "Rss menu"
}

async def set_bot_commands(client):
    commands = []
    for name, value in inspect.getmembers(BotCommands):
        if name in COMMAND_DESCRIPTIONS:
            # Use the first command in case of aliases
            command_val = value[0] if isinstance(value, list) else value
            # Remove the command suffix for Telegram
            command = command_val.replace(Config.CMD_SUFFIX, "")
            description = COMMAND_DESCRIPTIONS[name]

            # Basic validation
            if 1 <= len(command) <= 32 and 1 <= len(description) <= 256:
                commands.append(BotCommand(command, description))

    if commands:
        await client.set_bot_commands(commands)
