import inspect
from pyrogram.types import BotCommand
from .bot_commands import BotCommands
from ...core.config_manager import Config

COMMAND_DESCRIPTIONS = {
    'LeechCommand': "Leech",
    'QbLeechCommand': "Leech torrent using qBittorrent",
    'JdLeechCommand': "Leech using jdownloader",
    'NzbLeechCommand': "Leech using sabnzbd",
    'YtdlLeechCommand': "Leech yt-dlp supported links",
    'CloneCommand': "Copy file/folder to Drive",
    'MirrorCommand': "Mirror",
    'QbMirrorCommand': "Mirror torrent using qBittorrent",
    'JdMirrorCommand': "Mirror using jdownloader",
    'NzbMirrorCommand': "Mirror using sabnzbd",
    'YtdlCommand': "Mirror yt-dlp supported links",
    'CountCommand': "Count file/folder from GDrive",
    'UserSetCommand': "User settings",
    'BotSetCommand': "Bot settings",
    'StatusCommand': "Get Mirror Status message",
    'SelectCommand': "Select files from torrent",
    'RssCommand': "Rss menu",
    'ListCommand': "Search files in Drive",
    'CancelTaskCommand': "Cancel a task",
    'CancelAllCommand': "Cancel all tasks",
    'ForceStartCommand': "Start task from queue",
    'DeleteCommand': "Delete file/folder from GDrive",
    'LogCommand': "Get the Bot Log",
    'AuthorizeCommand': "Authorize user or chat",
    'UnAuthorizeCommand': "Unauthorize user or chat",
    'ShellCommand': "Run commands in Shell",
    'AExecCommand': "Execute async function",
    'ExecCommand': "Execute sync function",
    'RestartCommand': "Restart the Bot",
    'RestartSessionsCommand': "Restart Telegram Session(s)",
    'StatsCommand': "Bot Usage Stats",
    'PingCommand': "Ping the Bot",
    'HelpCommand': "All cmds with description",
    'StartCommand': "Starts the bot",
    'AddSudoCommand': "Add sudo user",
    'RmSudoCommand': "Remove sudo user",
    'UsersCommand': "Show users settings",
    'ClearLocalsCommand': "Clear exec locals",
}

async def set_bot_commands(client):
    commands = []
    ordered_commands = [
        'LeechCommand', 'QbLeechCommand', 'JdLeechCommand', 'NzbLeechCommand', 'YtdlLeechCommand',
        'CloneCommand', 'MirrorCommand', 'QbMirrorCommand', 'JdMirrorCommand', 'NzbMirrorCommand',
        'YtdlCommand', 'CountCommand', 'UserSetCommand', 'BotSetCommand', 'StatusCommand',
        'SelectCommand', 'RssCommand', 'ListCommand', 'CancelTaskCommand', 'CancelAllCommand',
        'ForceStartCommand', 'DeleteCommand', 'LogCommand', 'AuthorizeCommand', 'UnAuthorizeCommand',
        'ShellCommand', 'AExecCommand', 'ExecCommand', 'RestartCommand', 'RestartSessionsCommand',
        'StatsCommand', 'PingCommand', 'HelpCommand', 'StartCommand', 'AddSudoCommand',
        'RmSudoCommand', 'UsersCommand', 'ClearLocalsCommand'
    ]

    bot_commands_map = {name: value for name, value in inspect.getmembers(BotCommands)}

    for name in ordered_commands:
        if name in COMMAND_DESCRIPTIONS and name in bot_commands_map:
            value = bot_commands_map[name]
            command_val = value[0] if isinstance(value, list) else value
            command = command_val.replace(Config.CMD_SUFFIX, "")
            description = COMMAND_DESCRIPTIONS[name]

            if 1 <= len(command) <= 32 and 1 <= len(description) <= 256:
                commands.append(BotCommand(command, description))

    if commands:
        await client.set_bot_commands(commands)
