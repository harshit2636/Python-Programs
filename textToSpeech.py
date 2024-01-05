import pyttsx3
if __name__ == '__main__':
    text_to_speech=pyttsx3.init()
    while(True):
        x = input("enter u want to speak:")
        if x == 'q':
            break
        text_to_speech.say(x)
        text_to_speech.runAndWait()
