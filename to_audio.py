from moviepy.editor import *

# #In case you want to download a video from YouTube:
# #after you downloaded the video, store it e. g. in the folder video_samples
# #For demonstration I use a greate experimental video from Leila Emami and Gordian Maugg. Leila is Screenwriter and Artificial Intelligence Specialist and you can get in touch with her on LinkedIn: https://www.linkedin.com/in/leila-emami-9a9691289

# video_file = "https://www.youtube.com/watch?v=I1YjnG4G-ZI"

# set the path to the video file
video_file = "./video_samples/drei_spatzen.webm"
# set name of the output file
output_file = "./audio_samples/die_drei_spatzen.wav"

#load the video clip 
video = VideoFileClip(video_file)

#extract the audio from the video
audio = video.audio

# Set the desired audio parameters
audio_params = {
    "codec": "pcm_s16le",
    "fps": 16000,  # Set the desired sampling rate: 16000 Hz
    # "fps": 8000,  # Alternatively, set the sampling rate to 8000 Hz
    "nchannels": 1,  # Mono audio
    "bitrate": "16k"  # Set the desired bitrate
}


audio.write_audiofile(output_file, codec=audio_params["codec"],fps=audio_params["fps"],nbytes=2,bitrate=audio_params["bitrate"])