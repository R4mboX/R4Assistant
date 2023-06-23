#-Settings
Path_App = None

#-Functions
def Say(SText):
    print("Dummy AudioController: Saying --> " + SText)

def Play(TPath):
    print("Dummy AudioController: Playing .wav Files not supported.")
    
def Init(TPath):
    global Path_App
    Path_App = TPath
    print("AC_Dummy initialized")
    
