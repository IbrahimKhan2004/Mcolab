import re
from bot.helper.ext_utils.bot_utils import humanbytes
from bot.helper.ext_utils.media_utils import get_media_info

def format_duration(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    return f"{hours:02d}h{minutes:02d}m"

async def format_caption(file_path, user_caption):
    file_name = file_path.split('/')[-1]
    media_info = await get_media_info(file_path)
    file_size = humanbytes(media_info[3])
    duration = format_duration(int(media_info[0]))

    if user_caption:
        caption = user_caption.replace('{filename}', file_name)
        caption = caption.replace('{size}', file_size)
        caption = caption.replace('{duration}', duration)

        quality_match = re.search(r'(480p|720p|1080p|2160p)', file_name, re.IGNORECASE)
        if quality_match:
            caption = caption.replace('{quality}', quality_match.group(1))

        season_episode_match = re.search(r'S(\d{2})\s?E(\d{2})', file_name, re.IGNORECASE)
        if season_episode_match:
            caption = caption.replace('{season}', season_episode_match.group(1))
            caption = caption.replace('{episode}', season_episode_match.group(2))

        lang_match = re.search(r'\[(.*?)\]', file_name)
        if lang_match:
            caption = caption.replace('{language}', lang_match.group(1))

        subtitle_match = re.search(r'ESub', file_name)
        if subtitle_match:
            caption = caption.replace('{subtitle}', 'ESub')
    else:
        caption = f"<code>{file_name}</code>"

    return caption
