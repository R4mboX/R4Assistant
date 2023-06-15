#-Bibliotheken importieren----------------------
import pyttsx3
import sounddevice as sd
import soundfile as sf
#-Say--------------------------------------------
def Say(SText):
    engine.say(SText)
    engine.runAndWait()
#-Play-------------------------------------------
def Play(TPath):
    data, fs = sf.read("/home/pi/Software/R4Home/Audio/"+ TPath)
    sd.play(data, fs)
    sd.wait()
#-Start------------------------------------------
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
engine.setProperty('voice', 'en')
engine.setProperty('rate', 120)