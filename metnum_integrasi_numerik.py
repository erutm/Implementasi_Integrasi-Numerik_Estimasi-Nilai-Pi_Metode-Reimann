#Implementasi Integrasi Numerik untuk Menghitung Estimasi nilai Pi

#Mencari nilai integral dari fungsi f(x) = 4 / (1 + x^2) dari 0 sampai 1
#Nilai referensi pi yang digunakan: 3.14159265358979323846

import numpy as np
import time

#Fungsi untuk menghitung integral menggunakan metode Reimann
def integrasi_reimann(N):
    a = 0
    b = 1
    h = (b - a) / N
    sum = 0
    for i in range(N):
        x = a + i * h
        sum += (4 / (1 + x**2)) * h
    return sum

#Fungsi untuk menghitung galat RMS
def galat_RMS(aproksimasi, referensi):
    return np.sqrt(np.mean((aproksimasi - referensi)**2))

#Fungsi untuk melakukan pengujian berbagai nilai N
def pengujian():
    referensi_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]
    
    for N in N_values:
        waktu_mulai = time.perf_counter()
        aproksimasi_pi = integrasi_reimann(N)
        waktu_selesai = time.perf_counter()
        
        error = galat_RMS(aproksimasi_pi, referensi_pi)
        waktu_eksekusi = waktu_selesai - waktu_mulai
        print(f"N = {N}")
        print(f"Aproksimasi π: {aproksimasi_pi}")
        print(f"Galat RMS: {error}")
        print(f"Waktu Eksekusi: {waktu_eksekusi:.10f} detik\n")


#Jalankan pengujian
pengujian()