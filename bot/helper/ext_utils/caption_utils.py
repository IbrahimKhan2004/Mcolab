import re
from bot.helper.ext_utils.bot_utils import humanbytes
from bot.helper.ext_utils.media_utils import get_media_info

async def format_caption(file_path, user_caption):
    file_name = file_path.split('/')[-1]
    file_size = humanbytes((await get_media_info(file_path))[3])

    if user_caption:
        caption = user_caption.replace('{filename}', file_name)
        caption = caption.replace('{size}', file_size)

        duration_match = re.search(r'(\d{2})h(\d{2})m', file_name)
        if duration_match:
            caption = caption.replace('{duration}', f"{duration_match.group(1)}h {duration_match.group(2)}m")

        quality_match = re.search(r'(720p|1080p|2160p)', file_name)
        if quality_match:
            caption = caption.replace('{quality}', quality_match.group(1))

        season_episode_match = re.search(r'S(\d{2})E(\d{2})', file_name)
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
