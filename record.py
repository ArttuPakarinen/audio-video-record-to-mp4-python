import cv2
import sounddevice as sd
import wave
import numpy as np
import ffmpeg
import threading
import logging

# Audio configuration
FORMAT = np.int16
CHANNELS = 1  # Mono
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT = "output_audio.wav"

# Video configuration
VIDEO_OUTPUT = "output_video.avi"
FINAL_OUTPUT = "final_output.mp4"

# Global variable for recording state
recording = True

# Setup logging
logging.basicConfig(level=logging.INFO)

# List to hold recorded audio frames
recorded_frames = []

def audio_callback(indata, frames, time, status):
    if status:
        logging.warning(f"Audio status: {status}")
    recorded_frames.append(indata.copy())

def record_audio():
    global recording

    try:
        with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype=FORMAT, callback=audio_callback):
            logging.info("Recording audio...")
            while recording:
                sd.sleep(50)
    except Exception as e:
        logging.error(f"Error during audio recording: {e}")

    logging.info("Finished recording audio.")

    # Save audio to file only if recording was successful
    if recorded_frames:
        wf = wave.open(AUDIO_OUTPUT, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(RATE)
        wf.writeframes(np.concatenate(recorded_frames).astype(np.int16).tobytes())
        wf.close()
        logging.info("Audio file saved.")
    else:
        logging.error("No audio frames recorded.")

def record_video():
    global recording

    cap = cv2.VideoCapture(0)

    # Get video width, height, and FPS
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, fps, (width, height))

    logging.info(f"Recording video at {fps} FPS...")
    try:
        while recording:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    logging.info("Stopping recording...")
                    recording = False  # Stop both video and audio recording
                    break
            else:
                break
    except Exception as e:
        logging.error(f"Error during video recording: {e}")
    finally:
        logging.info("Finished recording video.")
        cap.release()
        out.release()
        cv2.destroyAllWindows()

# Start video recording in a separate thread
video_thread = threading.Thread(target=record_video)
video_thread.start()

# Start audio recording in the main thread
try:
    record_audio()
except KeyboardInterrupt:
    logging.info("Interrupted by user, stopping recording...")
    recording = False

# Wait for the video thread to finish
video_thread.join()

# Ensure the audio file was created
import os
if os.path.exists(AUDIO_OUTPUT):
    # Combine audio and video using ffmpeg
    input_video = ffmpeg.input(VIDEO_OUTPUT)
    input_audio = ffmpeg.input(AUDIO_OUTPUT)
    fps = cv2.VideoCapture(VIDEO_OUTPUT).get(cv2.CAP_PROP_FPS)
    ffmpeg.output(input_video, input_audio, FINAL_OUTPUT, vcodec='libx264', acodec='aac', r=fps).run()

    logging.info(f"Recording saved as {FINAL_OUTPUT}")
else:
    logging.error("Audio file was not created, cannot merge audio and video.")
