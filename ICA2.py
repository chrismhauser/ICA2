#============================================
# plotting in real time example

import time  # for sleeping
import random  # for generating random data
import numpy as np
from matplotlib import pyplot as plt
from collections import deque
import serial

serial_port = serial.Serial('/dev/cu.usbmodem1412', 57600, timeout=1)
serial_port.flush()

# create a queue of size N
size_of_queue = 3000
init_queue_value = -1
data = deque([init_queue_value] * size_of_queue)

# setup the figure to plot with
fig = plt.figure()

# setup the plot
# show at 0:20 on the x axis and 0:10 on y axis
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_xlim(0, 200)
ax1.set_ylim(0, 255)
line1, = plt.plot(data)  # get handle to the "line" that we use for updating the plot

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 200)
ax2.set_ylim(0, 255)
line2, = plt.plot(data)  # get handle to the "line" that we use for updating the plot

# do this until the queue is all filled in
try:
    while True:
        # get a random number
        # and add number to the queue
        bytes_to_read = serial_port.inWaiting()
        val = serial_port.read(bytes_to_read)
        if val:
            for value_as_int in val:
                value_as_int = ord(value_as_int)
                data.appendleft(value_as_int)
                data.pop()  # pop the last number off to keep queue size the same

        line1.set_ydata(data)  # set the data

        avg = np.average(data)
        line2.set_ydata(avg)  # set the data

        if(avg < 80): print "Grounded"
        elif (avg > 135): print "Touching"
        elif (avg > 110): print "Hovering"
        else: print "Normal"

        plt.draw()  # and draw it out

        #time.sleep(0.01)  # simulate some down time
        plt.pause(0.0001)
finally:
    serial_port.close()
