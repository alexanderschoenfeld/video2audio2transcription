# Video-to-Audio-to-Transcript
Github repo: [https://github.com/alexanderschoenfeld/video2audio2transcription](https://github.com/alexanderschoenfeld/video2audio2transcription)

Link: [ReadMe file](README_DE.md) in Deutsch

#### Prerequisits:
You need to have a **Microsoft Azure Account**, which you can get here: https://azure.microsoft.com/

In Azure you need to provision an **Azure AI Speech-Service** resource. The cost free tier F0 is sufficient to get started. More information here: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview.

Read these details about [Azure AI Speech Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/).

#### Software needed:
- [Visual Studio Code](https://code.visualstudio.com/) or another code editor of your choice
- [Python](https://www.python.org/) programming language installed on your system
- [MoviePy](https://pypi.org/project/moviepy/) a great Python based Video editing tool
- [Audacity](https://www.audacity.de/downloads/), a great open-source Audio tool
- [YT-DLP](https://github.com/yt-dlp/yt-dlp), a feature-rich command-line audio/video downloader
- [Azure Speech SDK](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-sdk)
- [Python-dotenv](https://pypi.org/project/python-dotenv/), Reads key-value pairs from a .env file and set them as environment variables

### 0. To get startet clone this repo to your local machine.

[Download Python](https://www.python.org/downloads/) and install it. With Python, you automatically install pip as well. Pip is the Python Package Manager, that helps to install all kinds of libraries and dependencies.

Open the terminal and you can check with `pip --version`, which version of you have installed currently.

Now, install all above mentioned dependencies with: `pip install azure-cognitiveservices-speech moviepy  yt-dlp python-dotenv`

##### In case you want to download a video from YouTube
- Run `yt-dlp -o video.mp4 https://www.youtube.com/watch?your-specific-video-path`
- Save that downloaded video e. g. into the folder **video_samples** 

### 1. Simple extract Audio from Video file
Use **to_audio.py** to transfer any video to a single audio.wav file.

*Settings & parameters:*
Set the variables `video_file` and `output_file` in the code.
Execute it on the terminal with `python to_audio.py`.

### 2. Chunk multiple Audio files from Video file
Use **audio_chunk.py** to split a video file into multiple audio file segments. Execute it on the terminal with `python audio_chunk.py`.

*Settings & parameters:*
`video_path` (str): The file path to the video you want to extract audio from. 
`chunk_duration` (float): The length, in seconds, of each individual audio segment that will be created. 
`output_format` (str, optional): The format of the output audio files (e.g., ".wav", ".mp3"). It defaults to ".wav" if no other format is specified.

Once the operation is complete, a message is printed to confirm that the process was successful.

### 3. Transcribe the audio file to text
To transcribe your audio, you now need to set up the **Azure AI Speech-Service** as explained above. Do the following:
- rename the file *".env_example"* into *".env"*
- go to the Azure Portal and **copy the key** of the Azure AI Speech-Service.
- place the key in the *".env"* variable `SPEECH_KEY=your_speech_key_here`
- your are all set

Now you can run `python transcribe.py`
Note: **On Mac** or **Linux** the command is likely `python3 transcribe.py`



