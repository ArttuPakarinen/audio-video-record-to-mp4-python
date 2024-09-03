import sounddevice as sd
import numpy as np

RATE = 44100
CHANNELS = 1  # Mono
DURATION = 5  # Seconds

def test_audio_recording():
    print("Recording...")
    recording = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=CHANNELS, dtype=np.int16)
    sd.wait()
    print("Recording finished")

    # Listen to the recording (optional, requires sound playback configured)
    sd.play(recording, RATE)
    sd.wait()

test_audio_recording()
