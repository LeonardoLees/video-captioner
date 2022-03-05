import speech_recognition as sr
from os import path, system

# get the mp4 name from user
video_name = input("Video Name: ")

# convert mp4 to mp3
# command2mp3 = f"C:\\Users\\llf972175\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg -i {video_name}.mp4 audio.mp3"
command2mp3 = f"C:\\Users\\Administrator\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg -i {video_name}.mp4 audio.mp3"
system(command2mp3)

# convert mp3 to wav
# command2wav = "C:\\Users\\llf972175\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg -i audio.mp3 audio.wav"
command2wav = "C:\\Users\\Administrator\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg -i audio.mp3 audio.wav"
system(command2wav)

# use the audio file as the audio source
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
#try:
#    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

