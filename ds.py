import speech_recognition as sr  
import webbrowser
import subprocess
import time

#main_dict={'open google':webbrowser.open("https://www.google.co.in")}

main_list=['open google','open youtube','open songs','open song','change song','change songs','chain song']

if __name__ == "__main__":                                                                    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   
     
    try:
        x=r.recognize_google(audio)  
        x=x.lower()
        print(x)
        if x in main_list:
            if(x=='open google'):
                webbrowser.open("https://www.google.co.in")
            elif(x=='open youtube'):
                webbrowser.open("https://www.youtube.com")
            elif(x=='open songs' or x=='open song'):
                subprocess.Popen('explorer "C:\\Users\\hp\\Desktop\\utube"')
            elif(x=='change song' or x=='change songs' or x=='chain song'):
                subprocess.call("explorer C:\\Users\\hp\\Desktop\\songs.bat", shell=True)
            print("Success")
            time.sleep(5)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))