from pytube import YouTube
from tqdm import tqdm
import os
import requests
import datetime

# Function to mark video as downloaded or with error in links.md


def mark_status(link, status="[OK]", error=None):
    with open('links.md', 'r') as file:
        lines = file.readlines()

    with open('links.md', 'w') as file:
        for line in lines:
            if line.strip() == link.strip():
                if error:
                    file.write(f"[ERROR:{error}] {link}\n")
                else:
                    file.write(f"{status} {line}")
            else:
                file.write(line)

# Function to check if a video already exists


def video_exists(link):
    return os.path.exists(f"{link}.mp4")

# Function to download YouTube videos with progress bar


def download_video(link):
    try:
        yt = YouTube(link)
    except Exception as e:
        print(f"Connection Error: {e}")
        mark_status(link, "[ERROR]", str(e))
        return False

    try:
        print(f"Downloading: {yt.title} - {link}")
        stream = yt.streams.filter(
            progressive=True, file_extension='mp4').order_by('resolution')[-1]

        # Get the video size
        video_size = stream.filesize

        response = requests.get(stream.url, stream=True)

        with open(f"{yt.title}.mp4", 'wb') as file, tqdm(
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

# Function to process links from links.md


def process_links():
    with open('links.md', 'r') as link_file:
        for line in link_file:
            if line.startswith("#"):
                continue  # Skip commented lines

            link = line.strip()

            if not link:
                continue  # Skip empty lines

            if video_exists(link):
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
