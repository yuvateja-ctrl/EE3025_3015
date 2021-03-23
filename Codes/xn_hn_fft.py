import numpy as np
import matplotlib.pyplot as plt
h = np.zeros(l)
h[0] = (b[0]/a[0])
h[1] = (1/a[0])*(b[1]-a[1]*h[0])
h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0])
h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0])
h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
		-a[4]*h[0])
for i in range(5,l):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
			a[4]*h[i-4])
			
X = np.fft.fftshift(np.fft.fft(x))
H = np.fft.fftshift(np.fft.fft(h))

plt.figure(1)
plt.plot(np.abs(X))
plt.title(r'$|X(k)|$')
plt.grid()

plt.figure(2)
plt.plot(np.angle(X))
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.figure(3)
plt.plot(np.abs(H))
plt.title(r'$|H(k)|$')
plt.grid()

plt.figure(4)
plt.plot(np.angle(H))
plt.title(r'$\angle{H(k)}$')
plt.grid()

#termux
plt.savefig('../figs/xnhnfft.pdf')
plt.savefig('../figs/xnhnfft.eps')
subprocess.run(shlex.split("termux-open ../figs/xnhnfft.pdf"))


#else
#plt.show()
