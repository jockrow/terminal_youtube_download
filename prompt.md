I have this file named youtubeDownload.py:
that process this another file that have the youtube links named: links.md
```markdown
from pytube import YouTube

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
        # TODO: validate links.md if is this not found or is empty
        # TODO: show progress bar for each download and if is n of m files
        # TODO: show for each link download 1/100
        # TODO: when the video is fisished downloaded for each file in links.md, mark it as [OK]
        # TODO: comment the lines downloaded sucessfuly in links.md and put the title commented right
        # TODO: avoid download the lines started with #
        # TODO: if exists any file, jump to the next url and mark it in links.md as this exists
        # TODO: put time at begining and final of the proccess
    except:
        print("Some Error!")

# TODO: put time at begining and final of the proccess
print('Task Completed! 👍')
```

this is my another file links.md
```markdown



https://www.youtube.com/shorts/qcIbDfYbWFo
https://www.youtube.com/shorts/PDJnEem-fSY

#https://www.youtube.com/shorts/ga4xVHfYf-Y
https://www.youtube.com/shorts/ilnDtcu5bhA

https://www.youtube.com/shorts/PDJnEem-fSY
https://www.youtube.com/shorts/LrjQQ6dZrQU




```

When finished the process, the file must to be:
```markdown
[OK] https://www.youtube.com/shorts/qcIbDfYbWFo
[OK] https://www.youtube.com/shorts/PDJnEem-fSY
#https://www.youtube.com/shorts/ga4xVHfYf-Y
[OK] https://www.youtube.com/shorts/ilnDtcu5bhA
[DUPLICATED LINE] https://www.youtube.com/shorts/PDJnEem-fSY
[OK] https://www.youtube.com/shorts/LrjQQ6dZrQU
```
