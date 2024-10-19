# Video-zu-Audio-zu-Transkript
GitHub-Repo: [https://github.com/alexanderschoenfeld/video-audio-transcription](https://github.com/alexanderschoenfeld/video-audio-transcription)

#### Voraussetzungen:
Du benötigst ein **Microsoft Azure-Konto**, welches du hier erhalten kannst: https://azure.microsoft.com/

In Azure musst du eine **Azure AI Speech-Service**-Ressource bereitstellen. Der kostenlose Tarif F0 ist ausreichend, um zu starten. Mehr Informationen hier: https://learn.microsoft.com/de-de/azure/ai-services/speech-service/overview.

Lies diese Details zu den [Azure AI Speech-Preisen](https://azure.microsoft.com/de-de/pricing/details/cognitive-services/speech-services/).

#### Benötigte Software:
- [Visual Studio Code](https://code.visualstudio.com/) oder ein anderer Code-Editor deiner Wahl
- Die Programmiersprache [Python](https://www.python.org/) muss auf deinem System installiert sein
- [MoviePy](https://pypi.org/project/moviepy/), ein großartiges Python-basiertes Videobearbeitungs-Tool
- [Audacity](https://www.audacity.de/downloads/), ein hervorragendes Open-Source-Audiotool
- [YT-DLP](https://github.com/yt-dlp/yt-dlp), ein funktionsreiches Kommandozeilen-Tool zum Herunterladen von Audio/Video
- [Azure Speech SDK](https://learn.microsoft.com/de-de/azure/ai-services/speech-service/speech-sdk)
- [Python-dotenv](https://pypi.org/project/python-dotenv/), liest Schlüssel-Wert-Paare aus einer .env-Datei und setzt sie als Umgebungsvariablen

### 0. Um zu starten, klone dieses Repo auf deinen lokalen Rechner.

[Python herunterladen](https://www.python.org/downloads/) und installieren. Mit Python wird auch automatisch pip installiert. Pip ist der Python-Paketmanager, der hilft, Bibliotheken und Abhängigkeiten zu installieren.

Öffne das Terminal und überprüfe mit `pip --version`, welche Version du derzeit installiert hast.

Installiere nun alle oben genannten Abhängigkeiten mit: `pip install azure-cognitiveservices-speech moviepy yt-dlp python-dotenv`

##### Falls du ein Video von YouTube herunterladen möchtest
- Führe `yt-dlp -o video.mp4 https://www.youtube.com/watch?your-specific-video-path` aus.
- Speichere das heruntergeladene Video z. B. im Ordner **video_samples**

### 1. Einfaches Extrahieren von Audio aus einer Videodatei
Verwende **to_audio.py**, um ein beliebiges Video in eine einzelne audio.wav-Datei zu konvertieren.

*Einstellungen & Parameter:*
Setze die Variablen `video_file` und `output_file` im Code.
Führe das Skript im Terminal aus mit `python to_audio.py`.

### 2. Aufteilen von mehreren Audiodateien aus einer Videodatei
Verwende **audio_chunk.py**, um eine Videodatei in mehrere Audioteilsegmente aufzuteilen. Führe das Skript im Terminal aus mit `python audio_chunk.py`.

*Einstellungen & Parameter:*
- `video_path` (str): Der Dateipfad zum Video, aus dem du Audio extrahieren möchtest.
- `chunk_duration` (float): Die Länge in Sekunden jedes einzelnen Audioteils, das erstellt wird.
- `output_format` (str, optional): Das Format der Ausgabedateien (z. B. ".wav", ".mp3"). Standardmäßig wird ".wav" verwendet, falls kein anderes Format angegeben ist.

Sobald die Operation abgeschlossen ist, wird eine Meldung ausgegeben, die bestätigt, dass der Vorgang erfolgreich war.

### 3. Transkribieren der Audiodatei in Text
Um dein Audio zu transkribieren, musst du nun den **Azure AI Speech-Service** einrichten, wie oben beschrieben. Gehe wie folgt vor:
- Benenne die Datei *".env_example"* in *".env"* um.
- Gehe zum Azure-Portal und **kopiere den Schlüssel** des Azure AI Speech-Service.
- Füge den Schlüssel in die Variable *".env"* ein: `SPEECH_KEY=dein_speech_key_hier`
- Alles ist jetzt bereit.

Nun kannst du `python transcribe.py` ausführen.
Hinweis: **Auf Mac** oder **Linux** lautet der Befehl wahrscheinlich `python3 transcribe.py`.
