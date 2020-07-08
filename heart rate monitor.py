'''
The code below is used to include other files on the computer that allow you to
use the camera and senseHat components
'''
from sense_hat import SenseHat
import time
from picamera import PiCamera, Color, Lightness
import picamera.array as p




startTime = time.time() #captures the current time

timeout = time.time() + 60 * 0.25 #sets the timeout value to be 60 * 0.1 seconds after the captured start time
#what time works best?

sense = SenseHat() 
camera = PiCamera()

g = ( 100,90,83) #this makes the variable 'g' the colour red using the (red, green, blue) or rgb format. For example, (0,0,255) is blue
#what colour works best?

pixels = [g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g
        ] #this sets the colour of each pixel in the 8X8 led matrix on the sense hat

intensity = []
secs = []
data = []

time.sleep(2)

while True:
    
    sense.set_pixels(pixels)

    #the code below lets you measure the light intensity with the camera
    with p.PiRGBArray(camera) as out:
        camera.capture(out, 'rgb')
        secs.append((round(time.time()-startTime, 2)))
        intensity.append(round(out.array[:,:,0].mean(), 2)) #the "out.array[:,:,0]" measures the redness. change the 0 to a 1 for green or a 2 for blue
        data.append(((round(time.time()-startTime, 2)),round(out.array[:,:,0].mean(), 2)))

        print(round(time.time()-startTime, 2))
        print(round(out.array[:,:,1].mean(), 2))

    
    #the code below break out of the infinite loop after the time reaches the timeout that was set at the top.
    if time.time() >= timeout:
        sense.clear()
        camera.close()
        break


#the code below creates an excel-style document for graphing
with open('pulse.csv', 'w') as f: 
    for d in data:
        f.write(str(d) + ' \n ')

f.close()























    
