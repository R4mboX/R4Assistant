# R4Assistant
Amazon Echo Alternative based on Raspberry PI and Python Libraries.<br>
It's an Modular Approach, so it's highly customizable.<br>
I kept everything as simple as possible, so anyone can pick it up and make modifications.<br>
I don't plan to update this repository. But we will see what happens.<br>

Features: <br>
PicoVoice for WakeWord and Speech Recognition <br>
Pyttsx3 for Text-To-Speech <br>
OpenAI for AI Responses <br>

It's easy to change each module, if you prefer using Whisper, oobabooga, etc. instead. <br>

Hardware Requirements:<br>
  • Raspberry Pi 4. 3B should work too, but 4 is recommended for performance / temperature issues.<br>
  • Raspberry OS (64-Bit)<br>
  • Some fancy Raspberry Case with Cooling. You will have Wakeword Detection running locally 24/7.<br>
    I use the SunFounder Pironman Case, which does a good job and keeps everything at around 40-50°C.<br>
  • USB Speakers. Keep it simple.<br>
  • USB Microphone. Don't keep it simple.<br>

Installation:<br>
Install the Requirements:<br>
  sudo pip3 install openai<br>
  sudo pip3 install pvporcupine<br>
  sudo pip3 install pvleopard<br>
  sudo apt-get install python3-pyaudio<br>
  sudo pip3 install pvrecorder<br>
  sudo pip3 install pyttsx3<br>
  sudo pip3 install sounddevice<br>
  sudo pip3 install soundfile<br>
  sudo apt-get install espeak<br>
  sudo apt-get install libespeak-ng1<br>
  sudo apt-get install libasound2-dev<br>
  sudo pip3 install simpleaudio<br>

IF you want to use PicoVoice like me, sign up for a free account: <br>
https://picovoice.ai/<br>

! Get your API Keys. !<br>
We will use 2 PicoVoice Components. <br>
  Porcupine for Wakeword Detection. Your Assistant will be in Wakeword Detection Mode most of the time. Standard Bot-Name I also use as Wakeword is "Astra".<br>
  Leopard for Speech Recognition.<br>
The way PicoVoice works is, you personalized models on their website. You can finetune the Wakeword Model on their Website easily, so you get a very efficient way for local WakeWord Recognition on a Raspberry.<br>
! Create and Download Keyword-File for Porcupine and Model for Leopard !<br>
  https://console.picovoice.ai/ppn<br>
  https://console.picovoice.ai/cat<br>
! Download a Porcupine Model here: <br>
  https://github.com/Picovoice/porcupine/tree/master/lib/common<br>
If you run into Problems, look at the QuickStart Guide: <br>
  https://picovoice.ai/docs/quick-start/porcupine-python/<br>
  https://picovoice.ai/docs/quick-start/leopard-python/  <br>

Now let's look at the Code. <br>
Clone or Place this Repository on your Raspberry.<br>

The Mainscript to start / run is R4Master.py<br>
  ! Customize the Path: Path_App = "/home/pi/Software/R4Assistant/" !<br>
  After booting up, the Script will cycle through the Update() Function. What it does:<br>
    1. Wait for a recognized Speech-Command<br>
    2. Analyze the Command and get a Response (from OpenAI or SmartHomeController<br>
    3. Pass the Response to the AudioController (TTS-Engine)<br>
    
Open Libraries/SpeechRecognizer/SR_PicoVoice.py<br>
  ! Customize "porcupine = ..." and "leopard = ..." !<br>
    Add your PicoVoice API / Access Key.<br>
    Customize the Paths to Model Files.<br>
  Scroll down and look for that line: transcript, words = leopard.process_file('/home/pi/Software/R4Assistant/Audio/LastRecord.wav')<br>
    Make sure that Path is correct.<br>
    
Open Libraries/AudioController/AC_Light.py<br>
  Make sure the Path here is right: data, fs = sf.read("/home/pi/Software/R4Home/Audio/"+ TPath)<br>
  You can change TTS Language here: engine.setProperty('voice', 'en')<br>
  
Open Libraries/AI/AI_OpenAI.py<br>
  Enter your API Key. Check the Path.<br>
  You can Customize your Bots Name by Changing his Name in this File (Astra) and by Editing everything in Libraries/AI/Config/<br>
  
All right. That's it. <br>
Run R4Master.py<br>
Following will happen:<br>
  It will wait for WakeWord (Your customized Porcupine WakeWord)<br>
  After it heared the Wakeword it will say "Yes?" and then record 5 Seconds of Audio.<br>
  It will then Analyze the Audio.<br>
  It will either execute a SmartHome Command (if you implemented that) or lets ChatGPT create a Response. <br>
  It will then get back into WakeWord Mode.<br>
  
If you run into any Problems feel free to fix them xD<br>
You might ask for help in the Discussions Section. <br>
Currently there are problems running the Software as a Service. Audio Hardware isnt detected correctly that way. <br>
So you have to manually start that script after booting up your raspberry.<br>
  python3 R4Master.py<br>

Things I recommend to do: <br>
Replace the Confirmation Sound: "Yes?". Use a Sound File (.wav) and AudioController.Play("Path/To/File.wav")<br>
Create and implement your Smart-Home Script. Look at Libraries/SmartHome for an Example with Broadlink Devices (sudo pip3 install broadlink)<br>
If you want to use a Different AI (maybe something running locally) just create a new Module at Libraries/AI/ and import it in R4Master.py instead of AI_OpenAI.<br>
  Make sure to provide a DoPrompt(UserMessage): Function that returns a Response String.<br>

Have fun!
