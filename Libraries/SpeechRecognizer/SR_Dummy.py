#-Settings
Path_App = None

#-Functions
def GetCommand(AudioController):
    text = input("Enter some Text corresponding a Voice Command: ")
    return (text)

def Init(TPath):
    global Path_App
    Path_App = TPath
    print("SR_Dummy initialized")