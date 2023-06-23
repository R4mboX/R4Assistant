#-Import Libraries
import pyttsx3
import sounddevice as sd
import soundfile as sf

#-Settings
Path_App = None

#-Functions
def Say(TText):
    engine.say(TText)
    engine.runAndWait()

def Play(TFile):
    data, fs = sf.read(Path_App + TFile)
    sd.play(data, fs)
    sd.wait()
    
def Init(TPath):
    global Path_App
    Path_App = TPath + "Audio/"
    print("AC_Light initialized")
    
#-Start------------------------------------------
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
engine.setProperty('voice', 'en')
engine.setProperty('rate', 120)