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

x,fs = sf.read('Sound_Noise.wav')
sample_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/sample_freq

b,a = signal.butter(order,Wn,'low')

omega = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
z = np.exp(1j * omega)
H = H(z,b,a)
#subplots
plt.plot(omega,abs(H))
plt.title('Impulse Frequency Response')
plt.xlabel('$w$')
plt.ylabel('$H(jw)$')
plt.grid()# minor

#termux
plt.savefig('../figs/H(jw).pdf')
plt.savefig('../figs/H(jw).eps')
subprocess.run(shlex.split("termux-open ../figs/H(jw).pdf"))

#else
#plt.show()
