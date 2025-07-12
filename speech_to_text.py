import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 3.0  # Wait for 3 seconds of silence before ending the phrase

with sr.Microphone() as source:
    print("Listening... Please speak your sentence...")
    audio = recognizer.listen(source)

print("Recognizing...")
try:
    recognized_text = recognizer.recognize_google(audio, language="en-US")
    print("You said:", recognized_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))