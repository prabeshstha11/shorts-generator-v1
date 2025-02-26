from moviepy.editor import *


def add_text(input_path, output_path, text):
    video = VideoFileClip(input_path)

    def dim_frame(frame):
        return frame * 0.3

    dimmed_video = video.fl_image(dim_frame)

    font_path = "fonts/PTSerif-Regular.ttf"
    fontsize = 20
    clip_width = dimmed_video.size[0] - 40

    txt_clip = TextClip(
        text,
        fontsize=fontsize,
        color="white",
        font=font_path,
        method="caption",
        size=(clip_width, None),
    )

    txt_clip = txt_clip.set_position(("center", "center")).set_duration(
        dimmed_video.duration
    )

    video_with_text = CompositeVideoClip([dimmed_video, txt_clip])

    video_with_text.write_videofile(output_path, codec="libx264")
