import speech_recognition as sr

reck=sr.Recognizer()
with sr.Microphone() as source: # using microphone as Source
    print("Speak Anything : ")
    audio =reck.listen(source)

    try:
        text=reck.recognize_google(audio)  #google api
        
        print("You said : {}".format(text))

    except:
        print("Sorry could not recongnize your voice")
