import numpy as np 
import matplotlib.pyplot as plt 
from dft import dft

t, _ = np.loadtxt("DFT_data.dat", unpack=True)
N = len(t)
dt = t[1] - t[0]
T = N * dt

sigma = 100e-3
A = 1.0

samples = A * np.exp(-t ** 2 / (2 * sigma**2))

spectrum = dft(samples)

p = np.arange(N)
omega = 2 * np.pi * p / T
p_pos = np.arange(N // 2 + 1)
omega_pos = omega[p_pos]
magnitude = np.abs(spectrum[p_pos])

plt.stem(omega_pos, magnitude)
plt.show()


