import yt_dlp

url = input("Enter YouTube URL: ")

options = {
    'format': 'best'
}

with yt_dlp.YoutubeDL(options) as downloader:

    downloader.download([url])

print("High Resolution Video Downloaded Successfully!")