from picamera import PiCamera
from time import sleep

camera = PiCamera()

#preview works only if the monitor is attached to the raspberry
def start_preview(camera,seconds):
    camera.start_preview()
    sleep(10)
    camera.stop_preview()

def set_rotation(camera,degrees):
    camera.rotation = degrees

def take_picture(camera,directory, sleep_time = 5):
    camera.start_preview()
    sleep(sleep_time)
    camera.capture(directory)
    camera.stop_preview()

def take_pictures_row(camera,directory, n_pictures = 5, sleep_time = 5):
    camera.start_preview()
    for i in range(n_pictures):
        sleep(sleep_time)
        camera.capture(directory % i)
        camera.stop_preview()

#directory h264
def record_video(camera,directory,duration):
    camera.start_preview()
    camera.start_recording(directory)
    sleep(duration)
    camera.stop_recording()
    camera.stop_preview()
