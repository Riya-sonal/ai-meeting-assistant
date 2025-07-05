import sounddevice as sd
import wavio
import tempfile

def record_audio_to_file(duration=5, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wavio.write(temp_file.name, audio, fs, sampwidth=2)
    return temp_file.name
