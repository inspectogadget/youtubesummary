from pytube import YouTube
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import speech_recognition as sr
import openai

# Download a video from YouTube
video_url = input("Enter the URL of the video you want to download: ")
try:
    yt = YouTube(video_url)
    video_stream = yt.streams.first()
    video_stream.download()
    print(f"Video '{yt.title}' has been downloaded successfully.")
except Exception as e:
    print(f"An error occurred while downloading the video: {e}")

# Extract the audio from the video
filename = "1.3gpp"
try:
    video = VideoFileClip(filename)
    audio = video.audio
    audio.write_audiofile(f"{filename}.mp3")
    print(f"Audio has been extracted from '{filename}' and saved as '{filename}.mp3'")
except Exception as e:
    print(f"An error occurred while extracting the audio: {e}")

# Convert the MP3 file to a WAV file
filename = "1.mp3"
try:
    mp3_file = AudioSegment.from_mp3(filename)
    wav_file_name = filename.replace(".mp3", ".wav")
    mp3_file.export(wav_file_name, format="wav")
    print(f"The MP3 file has been converted to a WAV file and saved as '{wav_file_name}'.")
except Exception as e:
    print(f"An error occurred while converting the MP3 file to a WAV file: {e}")

# Recognize the speech in the audio file and save the transcript
filename = "1.wav"
try:
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    text = r.recognize_sphinx(audio)
    with open("1.txt", "w") as file:
        file.write(text)
    print(f"Transcript has been saved to '1.txt'.")
except Exception as e:
    print(f"An error occurred while recognizing speech: {e}")

# Summarize the transcript using OpenAI
openai.api_key = "INSERT API-KEY HERE"
with open("1.txt", "r") as file:
    input_text = file.read()
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Please summarize the following text in bullet point form:\n\n" + input_text,
    max_tokens=1024,
    n=1,
    stop=None, 
    temperature=0.5,
)
bullet_points = response["choices"][0]["text"].strip()
with open("output.txt", "w") as file:
    file.write(bullet_points)
