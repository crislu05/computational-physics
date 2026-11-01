import numpy as np 
import matplotlib.pyplot as plt
from dft import dft


t, samples = np.loadtxt("DFT_data.dat", unpack=True)

N = len(t)
dt = t[1] - t[0]
T = N * dt 

spectrum = dft(samples)

p = np.arange(N)
omega = 2 * np.pi * p / T
p_pos = np.arange(N // 2 + 1)
omega_pos = omega[p_pos]
magnitude = np.abs(spectrum[p_pos])

plt.stem(omega_pos, magnitude)
plt.show()



# -----------
h_bar = 1.054571817e-34 

#step1: ignore peak at p = 0
omega_si = omega_pos * 1e12 

magnitude_no_dc = magnitude[1:]
omega_no_dc = omega_si[1:]
p_pos_no_dc = p_pos[1:]

idx = np.argsort(magnitude_no_dc)[::-1]

def B0_from_peak(omega, J=1, K=0):
    delta = J * (J + 1) - K * (K + 1)
    return h_bar * omega / delta 

peak = omega_no_dc[idx[0]]
B0 = B0_from_peak(peak)

print(B0)