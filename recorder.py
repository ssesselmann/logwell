#!/usr/bin/env python
## /src/py/recorder.py

'''
------SINGLE BUTTON AUDIO RECORDING DEVICE---------------------
This program runs after boot and waits for input on pin 33 True 
then records the stereo input from the USB sound card Line In
and saves the file to disc with the filename YYMMDD-HHMMSS.wav
stops recording when pin 33 is True and loops.
---------------------------------------------------------------
'''

#----------import libraries----------------------
import time
import sys
import datetime
import calendar
import RPi.GPIO as GPIO
import pyaudio
#import numpy
import wave
#import warnings
#import getopt

while True:
  #----------Define time variables-----------------
  currenttime=datetime.datetime.now()
  s=str(datetime.date.today().strftime("%y%m%d-"))
  t=str("%s%s%s"%(currenttime.hour,currenttime.minute,currenttime.second))
  e=str(".wav")

  #----------Define audio variables----------------
  CHUNK = 512
  FORMAT = pyaudio.paInt16
  CHANNELS = 1
  RATE = 48000 
  WAVE_OUTPUT_FILENAME = s+t+e
  p = pyaudio.PyAudio()

  #----------While loop start----------------------

  time.sleep(2)
  
  #clean up GPIO 
  GPIO.cleanup()

  GPIO.setmode(GPIO.BOARD)#Use RPi pin numbers
  GPIO.setwarnings(False)
  GPIO.setup(31,GPIO.OUT)#Setup pin 31 as OUT
  GPIO.setup(33,GPIO.IN)#Setup pin 33 as IN
  GPIO.setup(35,GPIO.OUT)#Setup pin 35 as OUT
  
  #Turn pin 31 output off
  GPIO.output(31, False)
  
  #Turn pin 35 output on
  GPIO.output(35, True)
  print ("\n\n Waiting for start signal: Yellow light is on\n")

  #Wait for pin 33 to go high
  while (GPIO.input(33) !=1):
  	pass

  #Turn pin 35 output off
  GPIO.output(35, False)
  print ("Yellow light off\n")

  #Turn pin 31 output on
  GPIO.output(31, True)
  print ("Recording sound file: Red light is on\n")
  time.sleep (1)
  
  #----------Start recording file here-----------
  
  stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK) 

  frames = []
  
  while (GPIO.input(33) !=1):
    	data = stream.read(CHUNK)
    	frames.append(data)
  	pass  #Pass when pin 33 to goes high
  	
  print "finished recording"
  #Turn pin 31 output off
  GPIO.output(31, False)
  print ("Red light turns off\n")       
  time.sleep(3)

  #----------Stop recording and update header ---

  stream.stop_stream()
  stream.close()
  p.terminate()
  
  wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()
  
  while (GPIO.input(33) !=0):
  	print("shutting down")
  	exit()
  pass     #Exit program when pin held for 5 seconds
  continue
#----------End of while loop---------------------

