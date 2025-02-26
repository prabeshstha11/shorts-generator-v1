import yt_dlp

def download_video(video_url):
    try:
        ydl_opts = {
            'outtmpl': './downloads/downloaded.mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            ydl.download([video_url])
            print("Download Completed!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
