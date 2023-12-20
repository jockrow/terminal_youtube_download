from pytube import YouTube

# SAVE_PATH = "./youtubeFolder"

link = open('links.md', 'r')

for i in link:
    try:
        yt = YouTube(i)
    except:
        print("Connection Error")
    try:
        print("..." + yt.title)
        print(i)
        # TODO: show the time elapsed for each file
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution')[-1].download()
        # for i in yt.streams.filter(progressive=True, file_extension='mp4'): print(str(i.resolution))
        # for i in yt.streams.filter(progressive=True, file_extension='mp4'):
        # .order_by('resolution')
        # 	print(str(i.resolution))
        # TODO: trim the file and remove the spaces
        # TODO: validate links.md if is this not found or is empty
        # TODO: show progress bar for each download and if is n of m files
        # TODO: show for each link download 1/100
        # DONE: when the video is fisished downloaded for each file in links.md, mark it as [OK]
        # TODO: comment the lines downloaded sucessfuly in links.md and put the title commented right
        # TODO: avoid download the lines started with #
        # TODO: if exists any file, jump to the next url and mark it in links.md as this exists
        # DONE: put time at begining and final of the proccess

        # stream = yt.streams.first()
        # print(stream)
        # stream.download(SAVE_PATH)
    except:
        print("Some Error!")

# TODO: put time at begining and final of the proccess
print('Task Completed! 👍')

# 144p
# 360p
# 720p
# 720p
# 720p
# 480p
# 480p
# 360p
# 360p
# 240p
# 240p
# 144p
# 144p
# None
# None
# None
# None
# None
