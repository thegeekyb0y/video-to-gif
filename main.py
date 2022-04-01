from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("my-life.mp4")

videoClip.write_gif("my-life.gif")
