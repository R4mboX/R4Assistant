#-Imports---------------------------------------
import pvporcupine
import pvleopard
import pvrecorder
import pyaudio
import struct
import wave
#-Instances-------------------------------------
porcupine = pvporcupine.create(
        access_key='ENTER YOUR PICOVOICE ACCESS KEY',
        keyword_paths=['/home/pi/Software/R4Home/Models/PicoVoice/Astra.ppn'],
        model_path='/home/pi/Software/R4Home/Models/PicoVoice/porcupine_params_de.pv')
leopard = pvleopard.create(
    access_key='ENTER YOUR PICOVOICE ACCESS KEY',
    model_path='/home/pi/Software/R4Home/Models/PicoVoice/Leo.pv')

pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length)  
#-Settings--------------------------------------
CHANNELS = 1
RATE = porcupine.sample_rate
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
        audio_frame = audio_stream.read(porcupine.frame_length)
        audio_frame = struct.unpack_from("h" * porcupine.frame_length, audio_frame)
        keyword_index = porcupine.process(audio_frame)
        if keyword_index == 0:
            StopStream()
            break;
        
def TranscribeVoice():
    StartStream()
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_TIME)):
        data = audio_stream.read(CHUNK)
        frames.append(data)
        
    wf = wave.open("Audio/LastRecord.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    transcript, words = leopard.process_file('/home/pi/Software/R4Assistant/Audio/LastRecord.wav')
    wordarray = transcript.split()
    StopStream()
    return wordarray

def StartStream():
    global audio_stream
    
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

def StopStream():
    global audio_stream
    audio_stream.close()