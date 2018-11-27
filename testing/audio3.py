import pyaudio
import numpy as np
import winsound
import struct
import math

def play_tone(frequency, amplitude, duration, fs, stream):
    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs
    # 1 cycle
    tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
            for n in xrange(N))
    # todo: get the format from the stream; this assumes Float32
    data = ''.join(struct.pack('f', samp) for samp in tone)
    for n in xrange(T):
        stream.write(data)

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK,output=True)
data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
peak=np.average(np.abs(data))*2
bars="#"*int(50*peak/2**16)
print("%04d %05d %s"%(i,peak,bars))
#winsound.Beep(int(peak),10)
#play_tone(peak, 0.1, 0.005, RATE, stream)

stream.stop_stream()
stream.close()
p.terminate()