# CODE FOR THE RASPBERRY PI CAMERA
from picamera import PiCamera
import time

# Create the instance of the camera
camera = PiCamera()

# Change the resolution
camera.resolution = (640, 480)

# Flip the CAMERA (vERTICAL)
camera.vflip = True

# Flip the CAMERA   (hORIZONTAL)
camera.hflip = True

# view the contents with the camera
camera.start_preview()
time.sleep(2)
camera.stop_preview()

# Take a photo
camera.capture("Picture.jpg")

# Record video
camera.start_recording("My_video.h264")
time.sleep(5)
camera.stop_recording()
