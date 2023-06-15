#-Import Libraries--------------------------
#-General-
import threading
import queue
#-Modules-
#import Libraries.SmartHome.SC_BroadLink as SmartController     # CUSTOMIZE FOR SMARTHOME-STUFF
import Libraries.SpeechRecognizer.SR_PicoVoice as SpeechRecognizer
import Libraries.AudioController.AC_Light as AudioController
import Libraries.AI.AI_OpenAI as AIController
#-Settings----------------------------------
#-General-
Path_App = "/home/pi/Software/R4Assistant/"
#-Update------------------------------------
def Update():
    while True:
        Command = SpeechRecognizer.GetCommand(AudioController)
        Response = AnalyzeCommand(Command)
        AudioController.Say(Response)
#-Funktionen-------------------------------------    
def AnalyzeCommand(Command):
    UnknownCommand = True
    
    if Command == "":
        UnknownCommand = False
        return "No Speech recognized."
    
    # Add SmartHome Functionality here:
    #if "lampe" in Command.lower() or "licht" in Command.lower():
    #    UnknownCommand = False
    #    Result = SmartController.AnalyzeCommand(Command)
    #    return Result
        
    if UnknownCommand == True:
        Response = AIController.DoPrompt(Command)
        return Response
#-Start----------------------------
AudioController.Say("Ready.")
Update()