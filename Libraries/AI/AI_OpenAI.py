#-Import Libraries--------------------------
import openai
import queue
import os
#-Settings----------------------------------
openai.api_key = "ENTER YOUR OPENAI API KEY HERE"
gptmodel = "gpt-3.5-turbo"
Path_App = None
Botname = None
History = []
Context = ""
Character = ""
Rules = ""
Instructions = ""
#-Functions---------------------------------
def DoPrompt(UserMessage):
    print("User: " + UserMessage)
    Prompt = Context + "\n \n" + Character + "\n \n" + Rules + "\n \n" + "Chathistory between " + Botname + " and User: \n" + '\n'.join(History) + "\n \n" + Instructions + "\n \n User: " + UserMessage + "\n " + Botname + ": "
    Completion = openai.ChatCompletion.create(
        model=gptmodel,
        messages=[
            {"role": "user", "content": Prompt}])
    try:
        Response = Completion.choices[0].message.content
        if Response.startswith(Botname +": "):
            Response = Response[len(Botname + ": "):]
        print(Botname + ": " + Response)
        History.append("User: " + UserMessage)
        History.append(Botname + ": " + Response)
        if len(History) > 100:
            History.pop(0)
            History.pop(0)
        SaveHistory()
        return Response
    except Exception as e:
        return "Error, try again."
        
def SaveHistory():
    with open(Path_App + "Config/History.txt", 'w') as file:
        for item in History:
            file.write(item + '\n')
            
def LoadConfig():
    global Context, Character, Rules, Instructions, History
    
    if os.path.exists(Path_App + "Config/History.txt"):
        with open(Path_App + "Config/History.txt", 'r') as file:
            for line in file:
                History.append(line.strip())
    else:
        with open(Path_App + "Config/DefaultHistory.txt", 'r') as file:
            for line in file:
                line = line.replace("BOTNAME", Botname)
                History.append(line.strip())
    
    with open(Path_App + "Config/Context.txt", 'r') as file:
        Context = file.read()
        Context = Context.replace("BOTNAME", Botname)

    with open(Path_App + "Config/Character.txt", 'r') as file:
        Character = file.read()
        Character = Character.replace("BOTNAME", Botname)

    with open(Path_App + "Config/Rules.txt", 'r') as file:
        Rules = file.read()
        Rules = Rules.replace("BOTNAME", Botname)

    with open(Path_App + "Config/Instructions.txt", 'r') as file:
        Instructions = file.read()
        Instructions = Instructions.replace("BOTNAME", Botname)
        
def Init(TPath, TBotname):
    if openai.api_key == "ENTER YOUR OPENAI API KEY HERE":
        print("Please set your API-Key at AI_OpenAI.py")
        exit()
    global Path_App, Botname
    Path_App = TPath + "Libraries/AI/"
    Botname = TBotname
    LoadConfig()
    print("AI_OpenAI initialized")