from win32com.client import Dispatch
import pygame
import time


spk1 = ("Enter What can I speak for you, Thank you.")
spk2 = ("Tahil is a 16 years old boy was born in january14 in 2005, " 
       "Who study in oasis public school and like to study Maths,Science and Programming, he is very Innocent, he also "
        "like to watch movies, WWE and other more things, his Best WWE Superstars are Roman Reins, Brock lesnar,"
        " John cena, The Undertaker, Goldberg and Drew Macyntyre and more, He like to learn Maths and Programming"
        "sommetimes science, his Best friends are Aarif, fareed, moosa, hannan, humayu baig, usman, owais, Aatif,"
        "Kaif, Rahil, mehfooz, talha, Zeeshan, Anas and many more")


def speak(str):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(str)

    print("1. Press Number(1) for Jarves to give intro....")
    print("2. press number(2) for Jarves to take input to (speak).")
    print("3. press number(3) for Jarves to Quit programme.")
    print("4. press number(4) for jarves to play CWj music.")
    print("5. press number(5) for jarves to stop CWj music.")
    print("6. press number(6) for jarves to play NCS music.")
    print("7. Press number(7) for jarves to stop Ncs music.")
    print("8. Press number(8) for Jarves to pause The music.")
    print("9. Press number(9) for Jarves to Resume The music.")
    print("10. Press number(10) for jarves to tell About (Tahil).\n")

    speaker.speak("Press any key to continue.")
    while(True):
        user_choice = input("Enter your Choice.")

        if user_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            speaker.speak("Not a Valid Option, Try again.")
            print("Not a Valid Option.")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice==1:
            speaker.speak(input("Enter (1) for intro."))
            pygame.mixer.init()
            pygame.mixer.music.load("Jarvis.mp3.mp3")
            pygame.mixer.music.play()
            time.sleep(19)
            pygame.mixer.stop()

        if user_choice==2:
            speaker.speak(spk1)
            speaker.speak(input("Enter your input."))

        if user_choice==4:
            pygame.mixer.init()
            pygame.mixer.music.load("CjW.mp3.mp3")
            speaker.speak("The CWJ Music is Playing now..")
            speaker.speak("Enter how many time you want to  play Music.")
            time.sleep(1)
            pygame.mixer.music.play(int(input("Enter Time in Numbers.")))

        if user_choice==5:
            speaker.speak("The CJW Music is stopping now..")
            pygame.mixer.music.stop()

        if user_choice==6:
            pygame.mixer.init()
            pygame.mixer.music.load("Ncs.mp3.mp3")
            speaker.speak("The NCS Music is playing now..")
            speaker.speak("Enter How many Times you want to play music.")
            time.sleep(1)
            pygame.mixer.music.play(int(input("Enter Time in numbers.")))

        if user_choice==7:
            speaker.speak("The Ncs music is stopping now..")
            pygame.mixer.music.stop()

        if user_choice==8:
            speaker.speak("The music is pause now..")
            pygame.mixer.music.pause()

        if user_choice==9:
            speaker.speak("The music is resume now..")
            pygame.mixer.music.unpause()

        if user_choice==10:
            speaker.speak(spk2)

        if user_choice==3:
            speaker.speak("The Programme is Quit now")
            exit()

if __name__=="__main__":
    speak("Hello Sir, I am Jarves The Computer Electronic Programme.")
