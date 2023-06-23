#-Imports
import pvporcupine
import pvleopard
import pvrecorder
import pyaudio
import struct
import wave
#-Settings
PVAccessKey = "Enter your PicoVoice Access Key"
Path_App = None
#-Instances-------------------------------------
Porcupine = None
Leopard = None
pa = pyaudio.PyAudio()
PyAudioStream = None
#-Settings--------------------------------------
CHANNELS = 1
CHUNK = 1024
FORMAT = pyaudio.paInt16
RECORD_TIME = 6

#-Functions-------------------------------------
def GetCommand(AudioController):
    WaitForWake()
    AudioController.Say("Yes?")
    Result = TranscribeVoice()
    return ' '.join(Result)
    
def WaitForWake():
    StartStream()
    while True:
        audio_frame = PyAudioStream.read(Porcupine.frame_length)
        audio_frame = struct.unpack_from("h" * Porcupine.frame_length, audio_frame)
        keyword_index = Porcupine.process(audio_frame)
        if keyword_index == 0:
            StopStream()
            break;
        
def TranscribeVoice():
    StartStream()
    frames = []
    for i in range(0, int(Porcupine.sample_rate / CHUNK * RECORD_TIME)):
        data = PyAudioStream.read(CHUNK)
        frames.append(data)
        
    wf = wave.open(Path_App + "Audio/LastRecord.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(Porcupine.sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    transcript, words = Leopard.process_file(Path_App + 'Audio/LastRecord.wav')
    wordarray = transcript.split()
    StopStream()
    return wordarray

def StartStream():
    global PyAudioStream
    
    PyAudioStream = pa.open(
        rate=Porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=Porcupine.frame_length)

def StopStream():
    global PyAudioStream
    PyAudioStream.close()
    
def Startup_Check():
    if PVAccessKey == "Enter your PicoVoice Access Key":
        print("Enter your Access Key at SR_PicoVoice.py and make sure you downloaded and placed the model files.")
        exit()
        
def Init(TPath):
    global Path_App, Porcupine, Leopard, PyAudioStream
    Path_App = TPath + "Libraries/SpeechRecognizer/"
    
    Porcupine = pvporcupine.create(
        access_key=PVAccessKey,
        keyword_paths=[Path_App + 'Models/Porcupine.ppn'])
        #model_path=Path_App + 'Models/Porcupine.pv') #INCLUDE IF USING OTHER LANGUAGE THAN en
    
    Leopard = pvleopard.create(
        access_key=PVAccessKey)
        #model_path=Path_App + 'Models/Leopard.pv') #INCLUDE IF USING OTHER LANGUAGE THAN en

    PyAudioStream = pa.open(
        rate=Porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=Porcupine.frame_length)
    
    print("SR_PicoVoice initialized")
    
#-Start
Startup_Check()