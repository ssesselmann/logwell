# logwell

Raspberry Pi single button recording device
-------------------------------------------
This program runs automatically after boot and waits for an input on pin 33 
If True then records the stereo input from a USB sound card (Line In)
and saves the file to disc with the filename YYMMDD-HHMMSS.wav
stops recording when pin 33 is True and loops.

Typical use case
----------------
This program was designed to work with the Gammaspectacular spectrometer for well logging.
1) Start recording
2) Lower detector a set distance into well at regular intervals
3) Stop recording
4) Use PRA (Pulse recorder and analyser) to parse spectrum iny=tervals and compare.

