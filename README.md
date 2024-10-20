# Python Video and Audio Recorder

This project is a Python script that simultaneously records video from a USB camera and audio from a microphone, and then combines them into a single `.mp4` file. It uses OpenCV for video capture, PyAudio for audio capture, and FFmpeg for merging the audio and video streams.

## Prerequisites

Before running the script, ensure that the following libraries and tools are installed on your system:

pip install opencv-python pyaudio numpy ffmpeg-python matplotlib


### Python Libraries

- `opencv-python`: For video capture and processing.
- `wave`: For saving audio files.
- `numpy`: For numerical operations.
- `ffmpeg-python`: For combining video and audio into an `.mp4` file.
- `threading`: For running video and audio capture simultaneously.
- `matplotlib`: En tiiä

Install the required Python packages using pip:

```bash
pip install opencv-python sounddevice numpy ffmpeg-python matplotlib


### System Dependencies
FFmpeg: A multimedia framework used to combine audio and video. Install it on Ubuntu with:
bash
Copy code
sudo apt-get install ffmpeg
PortAudio: Required for PyAudio. Install it on Ubuntu with:
bash
Copy code
sudo apt-get install portaudio19-dev
Usage
Clone this repository or copy the script to your local machine.

Ensure you have the required Python libraries and system dependencies installed.

Run the script:

bash
Copy code
python3 record.py
The script will start recording both audio and video simultaneously. Press Q button from the keyboard in the video window to stop recording.

Once the recording stops, the script will automatically combine the audio and video files into an .mp4 file named final_output.mp4.

### Customization
You can customize the following settings in the script:

Audio Settings:

FORMAT: Audio format (default is pyaudio.paInt16).
CHANNELS: Number of audio channels (default is 2 for stereo).
RATE: Sampling rate (default is 44100 Hz).
CHUNK: Buffer size (default is 1024).
Video Settings:

VIDEO_OUTPUT: File name for the raw video output (default is output_video.avi).
FINAL_OUTPUT: File name for the final combined video and audio output (default is final_output.mp4).
Stopping the Recording : Press Q button from the keyboard in the video window
Troubleshooting
PyAudio Installation Issues: If you encounter errors while installing pyaudio, ensure that the PortAudio development files are installed (sudo apt-get install portaudio19-dev).

ModuleNotFoundError for ffmpeg: Make sure to install the ffmpeg-python package using pip and verify that FFmpeg is installed on your system.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems.

Acknowledgments
OpenCV
PyAudio
FFmpeg


### Summary:

This `README.md` provides an overview of the project, instructions for installation, and usage guidelines. It also includes a section for troubleshooting common issues, customizing the script, and contributing to the project.

