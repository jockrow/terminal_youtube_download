from pytube import YouTube
from tqdm import tqdm
import os
import requests
import datetime
import re

input_file_path = "links.md"
output_file_path = input_file_path


def format_file():
    with open(input_file_path, "r") as infile:
        file_content = infile.read()

    # Trim the file and remove the spaces
    modified_content = re.sub(
        r"(^[ \t]*\n|[ \t]+|\&.*)", "", file_content, flags=re.MULTILINE
    )

    with open(output_file_path, "w") as outfile:
        outfile.write(modified_content)


def get_num_valid_videos():
    with open(input_file_path, "r") as infile:
        total_lines = sum(1 for line in infile)
        infile.seek(0)
        content = infile.read()
    count = len(re.findall(r"^\s*#", content, flags=re.MULTILINE))
    return total_lines - count


def mark_status(link, status="# [OK]", error=None):
    with open(input_file_path, "r") as file:
        lines = file.readlines()

    with open(input_file_path, "w") as file:
        for line in lines:
            if line.strip() == link.strip():
                if error:
                    file.write(f"# [ERROR:{error}] {link}\n")
                else:
                    file.write(f"# [{status}] {line}")
            else:
                file.write(line)


def download_video(link):
    try:
        yt = YouTube(link)
    except Exception as e:
        print(f"Connection Error: {e}")
        mark_status(link, "[ERROR]", str(e))
        return False

    try:
        print(f"Downloading: {yt.title} - {link}")
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by(
            "resolution"
        )[-1]

        video_size = stream.filesize

        response = requests.get(stream.url, stream=True)

        # progress bar
        with open(f"{yt.title}.mp4", "wb") as file, tqdm(
            desc=f"{yt.title}",
            total=video_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            # Download in chunks
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                bar.update(len(chunk))

        print("Downloaded successfully!")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        mark_status(link, "[ERROR]", str(e))
        return False


def process_links():
    with open(input_file_path, "r") as link_file:
        format_file()

        total_videos = get_num_valid_videos()
        print("total_videos:" + str(total_videos))

        for line in link_file:
            if line.startswith("#"):
                continue  # Skip commented lines

            link = line.strip()

            if not link:
                continue  # Skip empty lines

            if os.path.exists(f"{link}.mp4"):
                print(f"[EXISTS] {link}")
                mark_status(link, "[EXISTS]")
            else:
                if download_video(link):
                    mark_status(link)


# Main script
start_time = datetime.datetime.now()
print(f"Script started at: {start_time}")

process_links()

end_time = datetime.datetime.now()
print(f"Script completed at: {end_time}")
print(f"Total time taken: {end_time - start_time}")
