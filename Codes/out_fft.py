import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
def H(z,numerator,denominator):
    Numerator = np.polyval(numerator,pow(z,-1))
    Denominator = np.polyval(denominator,pow(z,-1))
    return Numerator/Denominator

input_signal,fs = sf.read('Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_frequency = 4000.0
Wn = 2*cutoff_frequency/sampl_freq

b,a = signal.butter(order,Wn,'low')

x = input_signal
l = len(x)
y = np.zeros(l)

w = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
z = np.exp(1j * w)
H = H(z,b,a)
X = np.fft.fftshift(np.fft.fft(x))
Y = np.multiply(X,H)
y = np.fft.ifft(np.fft.ifftshift(Y))
sf.write('Sound_fft.wav',np.real(y),fs)

plt.plot(np.real(y))
plt.title('Output signal through IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#termux
plt.savefig('../figs/ynfft.pdf')
plt.savefig('../figs/ynfft.eps')
subprocess.run(shlex.split("termux-open ../figs/ynfft.pdf"))
#else
#plt.show()
