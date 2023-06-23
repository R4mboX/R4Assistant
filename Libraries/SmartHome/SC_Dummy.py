#-Settings
Path_App = None

#-Functions
def AnalyzeCommand(Command):
    return "Dummy Smart-Home-Controller: Nothing to turn on / off here."
    
def Init(TPath):
    global Path_App
    PathApp = TPath
    print("SC_Dummy initialized")