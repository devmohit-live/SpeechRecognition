import speech_recognition as sr
r=sr.Recognizer()
PATH="" # enter your file path here
FILE=sr.AudioFile(PATH) 
with FILE as source:
    audio = r.record(source)
    try:
        l = r.recognize_google(audio)                  # generate a list of possible transcriptions
        print(l)
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")