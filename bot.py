import os
import sys
import speech_recognition as sr
import wikipedia 
import pyttsx3 as tts

r = sr.Recognizer()
verbs = {'run','open','send',"sign in"}
software_app = {'Chrome','Notepad', 'Zoom' , 'code','telegram','vlc' }
social_media = {"whatsapp","facebook","linkdin"}
whatsapp_contacts = {
    "shubham" : "+917218427013",
    "papa"    : "+919273946614"
}

def listen():
    """

    This function takes vocie as input from default microphone of machine.
    convert it into string and call parse function to take action on it.

    """
    with sr.Microphone() as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text =  r.recognize_google(audio,language="en-US")
        parse(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        tts.speak("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        tts.speak("Could not request results")


def parse(text_msg):

    """
    This function take string as input. Checks commands parse it and perform action on it.

    """
    words = set ( text_msg.lower().split())
    action = list(verbs & words)
    application = list(words & software_app)
    social_media_action = list(words & social_media )    
    result =  [elem for elem in software_app if elem in application]
 

    if ("what is" in text_msg):
        result = wikipedia.summary(text_msg, sentences = 2)  
        print(result)  
        tts.speak(result)
    elif("exit" in text_msg or "quite" in text_msg):
        sys.exit()
    elif("do not" in text_msg or "don't" in text_msg):
        pass    
    elif action and result:
        mystr=""
        for x in result:
            mystr += x + " && "  
        os.system((mystr[:-3]).lower())
        tts.speak("Running.. stay there")
    elif social_media_action :
        for app in social_media_action:
            if(app.lower() == "facebook"):
                os.system("chrome www.facebook.com")
                tts.speak("opening facebook.com for you.")
            elif(app.lower() == "linkedin"):
                os.system("chrome www.linkedin.com")
                tts.speak("opening linkedin for you")
            elif(app.lower()== "whatsapp"):
                if "shubham" in words:
                        os.system("chrome http://wa.me/"+whatsapp_contacts['shubham'])
                        tts.speak("sending whatsapp to shubham")
                if "papa" in words:
                        os.system("chrome http://wa.me/"+whatsapp_contacts['papa'])
                        tts.speak("sending whatsapp to papa")

    
if __name__ == "__main__":

    tts.speak("Welcome, What Can I do for you ?")
    
    """
    Listen for user command
    """
    
    while True:
        listen()