#!/usr/bin/env python
 
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os, datetime, sys

DEBUG = 1
GPIO.setmode(GPIO.BCM)


def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading


def saveData(filename, data, timestamp = True):
    try:
        f = open(filename, 'a')
        
        if timestamp:
            f.write(datetime.datetime.now() + ',')
            
        f.write(data + '\n')
    except:
        pass
    finally:
        try:
            f.close()
        except:
            pass


def main(filename = 'ldr.csv'):
    while True:
        t = RCtime(18)
        print(t)     # Read RC timing using pin 

        saveData(filename, t, True)
         

if __name__ == "__main__":
    if len(sys.argv) == 2:       
        filename = sys.argv[1]
      
        main(filename)
    else:
        print('enter the name of the file to save data into. Default: ldr.csv')
