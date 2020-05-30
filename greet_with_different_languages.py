print("HELLO WORLD! ")
from win32com.client import Dispatch
def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__=='__main__':
    speak("1 French ,Bonjour\
    2  Spanish ,Hola\
    3  Russian ,Zdravstvuyte\
    4 Chinese ,Nǐn hǎ\
    5 Italian ,Salve\
    6 Japanese ,Konnichiwa\
    7 German ,Guten Tag\
    8 Portuguese, Olá\
    9 Korean ,Anyoung haseyo\
    10 Arabic ,Ahlan\
    11 Danish ,Hej, Halløj\
    12 Swahili ,Shikamoo\
    13 Dutch ,Goedendag\
    14 Greek ,Yassas\
    15 Polish ,Dzień dobry\
    16 Indonesian ,Selamat siang\
    17 Hindi, Namaste, Namaskar\
    18 Turkish ,Merhaba\
    19 Hebrew ,Shalom\
    20 Sweden ,God dag\
    21 Norwegian, God dag ")