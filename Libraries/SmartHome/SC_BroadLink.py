import broadlink
import queue

WZL_Aktiv = True
KL_Aktiv = True
LampeWZ = ""
LampeKUE = ""

def AnalyzeCommand(Command):
    Result = "Unbekannter Smart-Home Befehl."
    
    if "wohnzimmer" in Command.lower():
        if "an" in Command.lower() or "ein" in Command.lower():
            Result = SwitchLight("Wohnzimmer", 1)
        if "aus" in Command.lower():
            Result = SwitchLight("Wohnzimmer", 0)       
            
    if "küche" in Command.lower():
        if "an" in Command.lower() or "ein" in Command.lower():
            Result = SwitchLight("Küche", 1)
        if "aus" in Command.lower():
            Result = SwitchLight("Küche", 0) 

    return Result

def SwitchLight(LampID, LampState):
    if LampID == "Wohnzimmer":
        if WZL_Aktiv == True:
            LampeWZ.set_state(pwr=LampState)
            return "OK."
        else:
            return "Wohnzimmerlampe ist nicht verbunden."
            
    if LampID == "Küche":
        if KL_Aktiv == True:
            LampeKUE.set_state(pwr=LampState)
            return "OK."
        else:
            return "Küchenlampe ist nicht verbunden."
    
def ChangeColor(LampID, TRed, TGreen, TBlue):
    Lampen[LampID].set_state(red=TRed)
    Lampen[LampID].set_state(green=TGreen)
    Lampen[LampID].set_state(blue=TBlue)
    Lampen[LampID].set_state(bulb_colormode=0)
    
def ColorOff(LampID):
    Lampen[LampID].set_state(bulb_colormode=1)

#-Start-------------------------------------
Lampen = []
try:
    LampeWZ = broadlink.hello('192.168.2.193')
    Lampen.append(LampeWZ)
except:
    print("SmartController: Wohnzimmerlampe nicht gefunden")
    WZL_Aktiv = False
    
try:
    LampeKUE = broadlink.hello('192.168.2.194')
    Lampen.append(LampeKUE)
except:
    print("SmartController: Küchenlampe nicht gefunden")
    KL_Aktiv = False

for Lampe in Lampen:
    Lampe.auth()
#    print(Lampe.get_state())
    
    
