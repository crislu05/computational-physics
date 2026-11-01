import numpy as np 


def dft(samples):
    """forward dft"""
    N =len(samples)
    spectrum = np.zeros(N, dtype=complex) #pre allocates a numpy array of length N filled with zero : [0. + 0.j, 0. + 0.j, ...]

    for p in range(N):
        total = 0
        for n in range(N):
            wave_val = np.exp(2j * np.pi * p * n / N)
            total += samples[n] * wave_val
        spectrum[p] = total 

    return spectrum 




def inverse_dft(spectrum):
    """backward dft"""
    N = len(spectrum)
    samples = np.zeros(N, dtype=complex)

    for p in range(N):
        total = 0
        for n in range(N):
            wave_val = np.exp(-2j * np.pi * p * n / N)
            total += spectrum[n] * wave_val
        samples[p] = total / N


    return samples 


def sample_signal(f, T, N):
    """samples a continous periodic function into N samples per period"""
    dt = T / N
    t = np.arange(N) * dt 
    samples = f(t)

    return t,samples 
