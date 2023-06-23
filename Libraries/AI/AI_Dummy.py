#-Settings
Path_App = None
Botname = None

#-Functions
def DoPrompt(UserMessage):
    return (Botname + ": No AI here!")

def Init(TPath, TBotname):
    global Path_App, Botname
    Path_App = TPath
    Botname = TBotname
    print("AI_Dummy initialized")

