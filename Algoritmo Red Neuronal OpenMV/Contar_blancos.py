# Untitled - By: joao - lun. ago. 24 2020

import sensor, image, time, math
thresholds = (245, 255)

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 3000) #Just to understand if the sensor needs time before start
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([thresholds], pixels_threshold=10, area_threshold=10, merge=True)
    for blob in blobs:
        img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=90, color=127)
    white_pixels = sum(blob.pixels() for blob in blobs)
    print(clock.fps(), white_pixels)
