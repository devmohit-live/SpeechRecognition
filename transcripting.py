'''
@Mohit : devmohit-live
This file generates transcript of audio file, and stores the transcript in Transcript.txt file
'''

import speech_recognition as sr
PATH=() #Path of your audio file 
#override \ with \\
r=sr.Recognizer()
f=open('Transcript.txt','w') #resultant file

with sr.AudioFile(PATH) as source:
    audio=r.record(source)

try:
    print('Success')
    print('Result stored in the Transcript file')
    f.write('audio file contains:\n\n'+r.recognize_google(audio))

except sr.UnknownValueError:   #For Lookup Error
    print('Google Speech Recognition could not understand your audio')

except sr.RequestError: #Request Error
    print("Couldn't get the results from google")
    
