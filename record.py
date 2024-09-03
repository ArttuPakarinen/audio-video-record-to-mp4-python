import cv2
import pyaudio
import wave
import numpy as np
import ffmpeg
import threading

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT = "output_audio.wav"

# Video configuration
VIDEO_OUTPUT = "output_video.avi"
FINAL_OUTPUT = "final_output.mp4"

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []

    print("Recording audio...")
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording audio.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save audio to file
    wf = wave.open(AUDIO_OUTPUT, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_video():
    cap = cv2.VideoCapture(0)

    # Get video width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, 20.0, (width, height))

    print("Recording video...")
    while recording:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    print("Finished recording video.")
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Threading to record audio and video simultaneously
recording = True
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=record_video)

audio_thread.start()
video_thread.start()

input("Press Enter to stop recording...")

recording = False

audio_thread.join()
video_thread.join()

# Combine audio and video using ffmpeg
input_video = ffmpeg.input(VIDEO_OUTPUT)
input_audio = ffmpeg.input(AUDIO_OUTPUT)
ffmpeg.output(input_video, input_audio, FINAL_OUTPUT, vcodec='libx264', acodec='aac').run()

print(f"Recording saved as {FINAL_OUTPUT}")
