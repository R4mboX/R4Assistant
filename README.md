# R4Assistant
An Speech Assistant based on Raspberry Pi and Python libraries, R4Assistant provides a modular approach, allowing for high customization. With simplicity at its core, anyone can easily modify this project according to their needs.<br>

## Features
* PicoVoice for WakeWord and Speech Recognition
* Pyttsx3 for Text-To-Speech
* OpenAI for AI Responses
* Chatbot with Personality (customizable) and stored Conversation-History <br>

It's easy to modify each module to use alternatives like Whisper, oobabooga, etc., based on your preference.

## Hardware Requirements
* Raspberry Pi 4 (3B could work, but 4 is recommended for better performance and temperature management)
* Raspberry OS (64-Bit)
* A well-cooled Raspberry Pi case (since WakeWord detection runs locally 24/7).
  - I use the SunFounder Pironman Case, which keeps the temperature around 40-50°C.
* Simple USB Speakers
* High-quality USB Microphone

## Installation
Install the necessary libraries:
* sudo apt-get install python3-pyaudio espeak libespeak-ng1 libasound2-dev
* sudo pip3 install openai pvporcupine pvleopard pvrecorder pyttsx3 sounddevice soundfile simpleaudio <br>

Clone this repository on your Raspberry Pi.<br>
Open/Edit R4Master.py <br>
Make sure "Path_App" contains the correct Folder. <br>

Now look at the Modules-Section. <br>
By Standard only Dummy Modules are active: <br>
```
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
#import Libraries.SmartHome.SC_BroadLink as SmartHomeController <br>
```

Currently using AC_Light, SR_PicoVoice and AI_OpenAI is recommended. <br>
Change it like that:

```
#-SpeechRecognizer
#import Libraries.SpeechRecognizer.SR_Dummy as SpeechRecognizer
import Libraries.SpeechRecognizer.SR_PicoVoice as SpeechRecognizer

#-AudioController
#import Libraries.AudioController.AC_Dummy as AudioController
import Libraries.AudioController.AC_Light as AudioController

#-AIController
#import Libraries.AI.AI_Dummy as AIController
import Libraries.AI.AI_OpenAI as AIController

#-SmartHomeController
import Libraries.SmartHome.SC_Dummy as SmartHomeController
#import Libraries.SmartHome.SC_BroadLink as SmartHomeController
```

The Dummy Modules are good for testing, since they provide very basic functionality. <br>

You will now have to set up PicoVoice -> [https://github.com/R4mboX/R4Assistant/wiki/PicoVoice-Setup](Click here for Tutorial) <br>
And add your OpenAI API Key at Libraries/AI/AI_OpenAI.py <br>

That's it! Now, run python3 **R4Master.py**. The following steps will occur: <br>

* The assistant waits for the WakeWord (your customized Porcupine WakeWord).
* After recognizing the WakeWord, it will respond with "Yes?" and then record 5 seconds of audio.
* The audio is then analyzed.
* It will either execute a SmartHome command (if implemented) or lets ChatGPT generate a response.
* The system will then revert to WakeWord Mode. <br>

Feel free to troubleshoot any issues you may encounter. You can also seek help in the Discussions section. Currently, there are problems running the software as a service as the audio hardware is not detected correctly in that mode. Thus, you need to manually start the script after booting up your Raspberry Pi.<br>

## Recommended Actions:
* Replace the confirmation sound "Yes?" with a .wav sound file using AudioController.Play("Path/To/File.wav")
* Implement your Smart-Home script. Refer to Libraries/SmartHome for an example using Broadlink Devices (install with sudo pip3 install broadlink)
* If you prefer using a different AI (possibly something running locally), create a new module at Libraries/AI/ and import it in R4Master.py instead of AI_OpenAI. Make sure to provide a DoPrompt(UserMessage): function that returns a Response String.
* To Customize the Personality of your new Assistant, look into the /AI/Config-Folder.<br>

Enjoy using R4Assistant!
