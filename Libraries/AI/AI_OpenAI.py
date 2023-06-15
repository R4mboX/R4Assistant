#-Import Libraries--------------------------
import openai
import queue
import os
#-Settings----------------------------------
openai.api_key = "ENTER YOUR OPENAI API KEY HERE"
gptmodel = "gpt-3.5-turbo"
Path_App = "/home/pi/Software/R4Home/Libraries/AI/"
History = []
Context = ""
Character = ""
Rules = ""
Instructions = ""
#-Functions---------------------------------
def DoPrompt(UserMessage):
    print("User: " + UserMessage)
    Prompt = Context + "\n \n" + Character + "\n \n" + Rules + "\n \n" + "Chathistory between Astra and User: \n" + '\n'.join(History) + "\n \n" + Instructions + "\n \n User: " + UserMessage + "\n Astra: "
    Completion = openai.ChatCompletion.create(
        model=gptmodel,
        messages=[
            {"role": "user", "content": Prompt}])
    try:
        Response = Completion.choices[0].message.content
        if Response.startswith("Astra: "):
            Response = Response[len("Astra: "):]
        print("Astra: " + Response)
        History.append("User: " + UserMessage)
        History.append("Astra: " + Response)
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
                History.append(line.strip())
    
    with open(Path_App + "Config/Context.txt", 'r') as file:
        Context = file.read()

    with open(Path_App + "Config/Character.txt", 'r') as file:
        Character = file.read()

    with open(Path_App + "Config/Rules.txt", 'r') as file:
        Rules = file.read()

    with open(Path_App + "Config/Instructions.txt", 'r') as file:
        Instructions = file.read()
#-Start-------------------------------------
LoadConfig()