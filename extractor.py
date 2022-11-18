import os
import json


def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url
    }


def extract_video_data_from_url(url):
    command = f'youtube-dl "{url}" -j --no-playlist'
    output = os.popen(command).read()
    video_data = json.loads(output)
    title = video_data["title"]
    formats = video_data["formats"]
    thumbnail = video_data["thumbnail"]
    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title": title,
        "formats": formats,
        "thumbnail": thumbnail
    }
