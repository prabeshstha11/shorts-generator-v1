from moviepy.editor import VideoFileClip


def trim_and_crop_video(input_path, output_path):
    try:
        video_clip = VideoFileClip(input_path)

        if video_clip.duration > 30:
            trimmed_clip = video_clip.subclip(0, 30)
        else:
            trimmed_clip = video_clip

        target_width = int(trimmed_clip.size[1] * (9 / 16))
        target_height = trimmed_clip.size[1]

        crop_left = (trimmed_clip.size[0] - target_width) // 2
        crop_right = trimmed_clip.size[0] - crop_left

        cropped_clip = trimmed_clip.crop(
            x1=crop_left, y1=0, x2=crop_right, y2=target_height
        )

        cropped_clip.write_videofile(
            output_path, codec="libx264", fps=24, preset="medium"
        )

        print("Tasks completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
