#-Modules------------------------------------------
# Uncommend one of each Module

#-SpeechRecognizer
import Libraries.SpeechRecognizer.SR_Dummy as SpeechRecognizer
#import Libraries.SpeechRecognizer.SR_PicoVoice as SpeechRecognizer

#-AudioController
import Libraries.AudioController.AC_Dummy as AudioController
#import Libraries.AudioController.AC_Light as AudioController

#-AIController
import Libraries.AI.AI_Dummy as AIController
#import Libraries.AI.AI_OpenAI as AIController

#-SmartHomeController
import Libraries.SmartHome.SC_Dummy as SmartHomeController
#import Libraries.SmartHome.SC_BroadLink as SmartHomeController

#-Settings
Path_App = "/Path/To/R4Assistant-Folder/"
Botname = "Astra"

#-Update------------------------------------
def Update():
    while True:
        Command = SpeechRecognizer.GetCommand(AudioController)
        Response = AnalyzeCommand(Command)
        AudioController.Say(Response)
#-Other Functions---------------------------    
def AnalyzeCommand(Command):
    UnknownCommand = True
    print ("Analyzing: " + Command)
    
    if Command == "":
        UnknownCommand = False
        return "No Speech recognized."
    
    if "light" in Command.lower():
        UnknownCommand = False
        Result = SmartHomeController.AnalyzeCommand(Command)
        return Result
        
    if UnknownCommand == True:
        Response = AIController.DoPrompt(Command)
        return Response
#-Start-----------------------------------
if Path_App == "/Path/To/R4Assistant-Folder/":
    print("Please set the Application-Path in R4Master.py")
    exit()
    
SpeechRecognizer.Init(Path_App)
AudioController.Init(Path_App)
SmartHomeController.Init(Path_App)
AIController.Init(Path_App, Botname)

AudioController.Say("Ready.")
print ("Running R4Assistant 0.0.2")
Update()