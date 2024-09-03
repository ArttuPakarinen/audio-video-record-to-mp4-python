import sounddevice as sd

print(sd.query_devices())  # List all devices
sd.default.device = 'Your USB Microphone Name'  # Set your specific microphone
