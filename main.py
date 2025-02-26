from video.video_downloader import download_video
from video.cropping import trim_and_crop_video
from video.adding_text import add_text
from video.backup import backup_download_folder


if __name__ == "__main__":
    backup_download_folder()

    video_url = input("Enter the YouTube video URL: ")
    text = input("Enter the quote you want to insert: ")

    download_video(video_url)

    trim_and_crop_video("./downloads/downloaded.mp4", "./downloads/cropped.mp4")

    add_text("./downloads/cropped.mp4", "./downloads/added_text.mp4", text)
