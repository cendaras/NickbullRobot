# Dataset Capture Script - By: lore - jue. oct. 29 2020

# Use this script to control how your OpenMV Cam captures images for your dataset.
# You should apply the same image pre-processing steps you expect to run on images
# that you will feed to your model during run-time.

import sensor, image, time, lcd
thresholds = (240, 255)
sensor.reset()                        # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.
lcd.init()
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    lcd.display(img)
    y=img.draw_line((120,0,120,240),color=(0,0,200))
    x=img.draw_line((0,120,320,120),color=(0,0,200))
    blobs = img.binary([(0,37)]).find_blobs([thresholds], pixels_threshold=10, area_threshold=10, merge=True)

    print(clock.fps())
