from moviepy.editor import VideoFileClip

# Example usage
video_path = "./video_samples/mysamplevideo.mp4"
chunk_duration = 30  # Chunk size in seconds

def chunk_audio(video_path, chunk_duration, output_format=".wav"):
    """
    Splits the audio from a video file into multiple segments and displays a confirmation message when the process is complete.

Parameters:
video_path (str): The file path to the video you want to extract audio from. This should be a string that specifies the location of the video file on your system.
chunk_duration (float): The length, in seconds, of each individual audio segment that will be created. For example, if set to 30.0, the audio will be split into 30-second chunks.
output_format (str, optional): The format of the output audio files (e.g., ".wav", ".mp3"). It defaults to ".wav" if no other format is specified.
This function extracts audio from a given video file, divides it into segments of the specified duration, and saves each segment in the specified format. Once the operation is complete, a message is printed to confirm that the process was successful.
    """
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio

        start_time = 0
        for _ in range(0, int(audio_clip.duration // chunk_duration)):
            end_time = start_time + chunk_duration
            chunk = audio_clip.subclip(start_time, end_time)
            chunk_filename = f"chunk_{start_time}.{output_format}"
            chunk.write_audiofile(chunk_filename)
            start_time += chunk_duration

        video_clip.close()  # Close the video clip
        print("Audio chunking completed!")
    except Exception as e:
        print(f"Error chunking audio: {e}")



chunk_audio(video_path, chunk_duration)
