# R4Assistant
An Amazon Echo alternative based on Raspberry Pi and Python libraries, R4Assistant provides a modular approach, allowing for high customization. With simplicity at its core, anyone can easily modify this project according to their needs.<br>
This repository may not be frequently updated, but the future is unpredictable.

## Features
* PicoVoice for WakeWord and Speech Recognition
* Pyttsx3 for Text-To-Speech
* OpenAI for AI Responses <br>

It's a easy to modify each module to use alternatives like Whisper, oobabooga, etc., based on your preference.

## Hardware Requirements
* Raspberry Pi 4 (3B could work, but 4 is recommended for better performance and temperature management)
* Raspberry OS (64-Bit)
* A well-cooled Raspberry Pi case (since WakeWord detection runs locally 24/7).
  - I use the SunFounder Pironman Case, which keeps the temperature around 40-50°C.
* Simple USB Speakers
* High-quality USB Microphone

## Installation
Install the necessary libraries:

* sudo pip3 install openai
* sudo pip3 install pvporcupine
* sudo pip3 install pvleopard
* sudo apt-get install python3-pyaudio
* sudo pip3 install pvrecorder
* sudo pip3 install pyttsx3
* sudo pip3 install sounddevice
* sudo pip3 install soundfile
* sudo apt-get install espeak
* sudo apt-get install libespeak-ng1
* sudo apt-get install libasound2-dev
* sudo pip3 install simpleaudio

For using PicoVoice as I do, sign up for a free account at https://picovoice.ai/ <br>
Obtain your API Keys and utilize two PicoVoice components:

* Porcupine for WakeWord detection. The Assistant stays in WakeWord detection mode most of the time. 
  - In Standard-Configuration I use the bot name "Astra" as the WakeWord.
* Leopard for Speech Recognition. <br>
PicoVoice allows you to personalize models on their website. This means you can easily fine-tune the WakeWord model for efficient local WakeWord recognition on a Raspberry Pi.

Customize and download the Keyword File for Porcupine and Model for Leopard from the following links: <br>
* https://console.picovoice.ai/ppn
* https://console.picovoice.ai/cat <br>
 
Download a Porcupine Model here:
* https://github.com/Picovoice/porcupine/tree/master/lib/common <br>

In case you encounter any issues, refer to the QuickStart Guide:
* https://picovoice.ai/docs/quick-start/porcupine-python/
* https://picovoice.ai/docs/quick-start/leopard-python/ <br>

Get your OpenAI API Key at https://openai.com/blog/openai-api.

Clone this repository on your Raspberry Pi. The main script to start/run is **R4Master.py**. <br>
Customize the path as follows: Path_App = "/home/pi/Software/R4Assistant/". <br>

Upon booting up, the script will continuously execute the Update() function which performs the following tasks:
* Waits for a recognized speech command
* Analyzes the command and gets a response (from OpenAI or SmartHomeController)
* Passes the response to the AudioController (TTS-Engine) <br>

Open *Libraries/SpeechRecognizer/SR_PicoVoice.py*. <br>
Customize "porcupine = ..." and "leopard = ..." by adding your PicoVoice API / Access Key and adjusting the paths to the model files. <br>
Ensure that the path in the line: <br>
transcript, words = leopard.process_file('/home/pi/Software/R4Assistant/Audio/LastRecord.wav') <br>
is correct.

Open *Libraries/AudioController/AC_Light.py*. <br>
Verify the path here: <br>
data, fs = sf.read("/home/pi/Software/R4Home/Audio/"+ TPath). <br>
You can also change the TTS language here with: engine.setProperty('voice', 'en').<br>

Open *Libraries/AI/AI_OpenAI.py*, enter your API Key, and check the path. <br>
Customize your bot's name by changing it in this file (Astra) and by editing everything in *Libraries/AI/Config/*. <br>

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
* If you prefer using a different AI (possibly something running locally), create a new module at Libraries/AI/ and import it in R4Master.py instead of AI_OpenAI. Make sure to provide a DoPrompt(UserMessage): function that returns a Response String.<br>

Enjoy using R4Assistant!
