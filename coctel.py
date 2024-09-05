# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import soundfile as sn
import numpy as np
from scipy.fft import fft, fftfreq
from sklearn.decomposition import FastICA
from scipy.signal import butter, lfilter

plt.close('all')

# Leer archivos de sonido
pim, Fs1 = sn.read('AUDIO_1.wav')
pum, Fs2 = sn.read('AUDIO_2.wav')
pam, Fs3 = sn.read('AUDIO_3.wav')
pim1, Fr1 = sn.read('RUIDO_1.wav')
pum2, Fr2 = sn.read('RUIDO_2.wav')
pam3, Fr3 = sn.read('RUIDO_3.wav')

# Verificar que todas las frecuencias de muestreo sean iguales
if not (Fs1 == Fs2 == Fr1 == Fr2):
    raise ValueError("Las frecuencias de muestreo no son iguales. No se puede continuar.")

# Encuentra la longitud mínima de las señales
min_length = min(len(pim), len(pum), len(pam))

# Recortar las señales para que tengan la misma longitud
pim_recortado = pim[:min_length]
pum_recortado = pum[:min_length]
pam_recortado = pam[:min_length]

# Mezcla de los audios recortados
audio_mezclado = pim_recortado + pum_recortado + pam_recortado

# Aplicación de ICA
ica = FastICA(n_components=3)
sources = ica.fit_transform(audio_mezclado.reshape(-1, 1))

# Selección de la fuente (ajustar el índice según sea necesario)
voz_filtrada = sources[:, 0]

# Recortar la señal de voz filtrada a 6 segundos
duracion_deseada = 7  # en segundos
nuevas_muestras = int(Fs1 * duracion_deseada)
voz_filtrada_recortada = voz_filtrada[:nuevas_muestras]

# Aplicar un filtro pasabanda para mejorar la calidad de la señal
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Definir los límites del filtro pasabanda para la voz humana
lowcut = 1500.0  # Frecuencia mínima en Hz
highcut = 3000.0  # Frecuencia máxima en Hz

# Aplicar el filtro pasabanda
voz_filtrada_mejorada = bandpass_filter(voz_filtrada_recortada, lowcut, highcut, Fs1)

# Normalizar la señal filtrada
voz_filtrada_mejorada /= np.max(np.abs(voz_filtrada_mejorada))

# Guardar el audio filtrado mejorado
sn.write('Vocecita.wav', voz_filtrada_mejorada, Fs1)

# Calcular el SNR para cada par de señales de audio y ruido
def calcular_snr(signal, noise):
    # Calcular la potencia de la señal
    potencia_signal = np.mean(signal**2)
    # Calcular la potencia del ruido
    potencia_noise = np.mean(noise**2)
    # Evitar división por cero
    if potencia_noise == 0:
        potencia_noise = np.finfo(float).eps
    # Calcular SNR en decibelios
    snr_db = 10 * np.log10(potencia_signal / potencia_noise)
    return snr_db

# Calcular SNR para cada par de señales de audio y ruido
snr_pim = calcular_snr(pim, pim1)
snr_pum = calcular_snr(pum, pum2)
snr_pam = calcular_snr(pam, pam3)

snr_pim1 = calcular_snr(voz_filtrada_mejorada, pim1)
snr_pum2 = calcular_snr(voz_filtrada_mejorada, pum2)
snr_pam3 = calcular_snr(voz_filtrada_mejorada, pam3)


print(f"El SNR entre la señal de audio 1 y el ruido 1 es: {snr_pim:.2f} dB")
print(f"El SNR entre la señal de audio 2 y el ruido 2 es: {snr_pum:.2f} dB")
print(f"El SNR entre la señal de audio 3 y el ruido 3 es: {snr_pam:.2f} dB")


print(f"El SNR entre Vocecita y el ruido 1 es: {snr_pim1:.2f} dB")
print(f"El SNR entre Vocecita y el ruido 2 es: {snr_pum2:.2f} dB")
print(f"El SNR entre Vocecita y el ruido 3 es: {snr_pam3:.2f} dB")

# Análisis temporal
timepim = np.arange(0, len(pim)) / Fs1
timepum = np.arange(0, len(pum)) / Fs2
timepam= np.arange(0, len(pam)) / Fs3

timepim1 = np.arange(0, len(pim1)) / Fr1
timepum2 = np.arange(0, len(pum2)) / Fr2
timepam3 = np.arange(0, len(pam3)) / Fr3

plt.figure(figsize=(10, 6))

plt.plot(timepim, pim, label='Voces Toma 1', color='pink')
plt.plot(timepum, pum, label='Voces Toma 2', color='red')
plt.plot(timepam, pam, label='Voces Toma 3', color='green')

plt.plot(timepim1, pim1, label='Ruido Toma 1', color='blue')
plt.plot(timepum2, pum2, label='Ruido Toma 2', color='brown')
plt.plot(timepam3, pam3, label='Ruido Toma 3', color='white')

plt.title("Análisis Temporal de Todas las Señales")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [mV]")
plt.legend()
plt.show()

# Análisis espectral usando FFT
N1 = len(timepim)
T1 = 1.0 / Fs1

N2 = len(timepum)
T2 = 1.0 / Fs2

N3 = len(timepam)
T3 = 1.0 / Fs3

Nr1 = len(timepim1)
Tr1 = 1.0 / Fr1

Nr2 = len(timepum2)
Tr2 = 1.0 / Fr2

Nr3 = len(timepam3)
Tr3 = 1.0 / Fr3

yf_pim= fft(pim)
yf_pum = fft(pum)
yf_pam = fft(pam)
yf_pim1 = fft(pim1)
yf_pum2 = fft(pum2)
yf_pam3 = fft(pam3)

xf_pim = fftfreq(N1, T1)[:N1//2]
xf_pum = fftfreq(N2, T2)[:N2//2]
xf_pam = fftfreq(N3, T3)[:N3//2]
xf_pim1 = fftfreq(Nr1, Tr1)[:Nr1//2]
xf_pum2 = fftfreq(Nr2, Tr2)[:Nr2//2]
xf_pam3 = fftfreq(Nr3, Tr3)[:Nr3//2]

plt.figure(figsize=(10, 6))

plt.plot(xf_pim, 2.0/N1 * np.abs(yf_pim[:N1//2]), label='Voces Toma 1', color='blue')
plt.plot(xf_pum, 2.0/N2 * np.abs(yf_pum[:N2//2]), label='Voces Toma 2', color='green')
plt.plot(xf_pam, 2.0/N3 * np.abs(yf_pam[:N3//2]), label='Voces Toma 3', color='red')

plt.plot(xf_pim1, 2.0/Nr1 * np.abs(yf_pim1[:Nr1//2]), label='Ruido Toma 1', color='orange')
plt.plot(xf_pum2, 2.0/Nr2 * np.abs(yf_pum2[:Nr2//2]), label='Ruido Toma 2', color='yellow')
plt.plot(xf_pam3, 2.0/Nr3 * np.abs(yf_pam3[:Nr3//2]), label='Ruido Toma 3', color='purple')

plt.title("Análisis Espectral usando FFT de Todas las Señales")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")
plt.legend()
plt.show()

# Graficar el audio filtrado 
plt.figure(figsize=(12, 6))
plt.plot(voz_filtrada_mejorada, color='violet')
plt.legend()
plt.title("Voz Filtrada usando ICA & Filtro Pasa Banda")
