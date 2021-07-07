from pytube import YouTube


def get_video(streams, res):
        stream = list(filter(lambda x: x.resolution == res, streams))
        return stream

# Input for youtube address.
video_address = input("Enter Youtube Video URL: ").strip()
youtube_var = YouTube(video_address)

# Input for the desired resolution for requested video.
video_res = input(f"Enter YouTube Video Resolution for {youtube_var.title}: ").strip()
stream_var = get_video(youtube_var.streams, video_res)[0]

# Connecting the download function to the stream variable.
stream_var.download()

print(f"YouTube Video {youtube_var.title} Downloaded With Resolution {video_res}")

