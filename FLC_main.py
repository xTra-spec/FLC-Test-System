"""
1. Mozliwość wyboru modelu jednostki, zaleznie od wyboru, zostaną dobrane odpowiednie nastawy generatora i wyniki PASS/FAIL (specyficzne informacje nt jednostki w oddzielnym pliku)
2. Uzytkownik moze wpisac numer seryjny, data to lokalny czas komputera
3. Sprzęt: Oscyloskop Teka, Generator, PC
4. Testy: Wykres liniowości wzmacniacza, pomiar BW, SLEW RATE
5. Check lista, infomacje jaki ustawić Rise/Fall time dla danej jednostki, nastawy genratora są wybierane automatycznie, program pokaze czy miesci sie w limitach
6. Automatyczne tworzenie certyfikatu kalibracji z wykresem liniowosci, zapis do pliku

"""
"""
print("FLC Testy system v0.1")

#unit_model = input("Wybierz typ jednostki:" "\nA400\nP100\nA800\n")
serial_number = "" 
while len(serial_number) != 6:
    serial_number = input("Wpisz Serial Number ") 
    if len(serial_number) == 6:
        print("Serial number OK")
    elif len(serial_number) < 6:
        print("Serial number jest zbyt krótki")
    elif len(serial_number) > 6:
        print("Serial number jest zbyt dlugi")
"""
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

"""

#import F10A
#max_output_vpp = 200

##################################### Linearity #########################################

import pyvisa

rm = pyvisa.ResourceManager()
rm.list_resources()
('GPIB0::28::INSTR')
gen = rm.open_resource('XXX')
#mso = rm.open_resource('YYY')

gen.write("*RST;*CLS")
gen.write("WAVE SQUARE;AMPUNIT VPP;FREQ 100000;OUTPUT ON")

vpp = 1
step_vpp = 1
measured_gen_vpp = []
measured_amp_vpp = []

while vpp <= 10: # sweep vpp to 10Vpp
    gen.write("AMPL " + str(vpp))
    sleep(0.1)
    if vpp <=10:
        x = mso.write(':READ?') #channel 1
        measured_gen_vpp.append(x)
    #mso.write(':READ?') #channel 2
    vpp += step_vpp


"""
amp_axis = []

for j in gen_axis:
    j *= gain
    amp_axis.append(j)

print(amp_axis)
print(gen_axis)


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([amp_axis])
ypoints = np.array([gen_axis])

plt.plot(amp_axis, gen_axis)
plt.title("Amplification Linearity")
plt.xlabel("Voltage Output")
plt.ylabel("Voltage Input")
plt.grid()
plt.show()
"""
##################################### Bandwith #########################################
"""
start_freq = 5 #khz
step_freq = 5 #khz
stop_freq = 1000 #khz

freq = []

for u in range(200):
    #start_vpp = str(start_vpp)
    freq.append(start_freq)
    start_freq += step_freq
    #start_vpp = int(start_vpp)

print(freq)

voltage = 800
amplitude = []

for z in range(200):
    amplitude.append(voltage)
print(amplitude)


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
x = freq
y = amplitude
plt.figure(figsize=(10,5))
plt.semilogx(x, y)
plt.ylabel('Amplitude [Vpp]')
plt.xlabel('Frequency [kHz]')
plt.title('Frequency response')
plt.grid(which='both', linestyle='-', color='grey')
plt.xticks([10, 100, 1000, 10000], ["10", "100", "1000", "10000"])
plt.show()
"""

"""
#ZASYMULOWAĆ DANE DO WYKRESU FREQUENCY RESPONSE
#ABY WYKRES DZIALAL, MUSY BYC TYLE SAMO ELEMENTOW NA OSI X I Y
#DLA CZĘSTOTLIWOŚCI, ZACZYNAM OD 5KHZ I LOGARYTMICZNIE ZWIEKSZAM CZĘSTOTLIWOŚĆ A DOJDĘ DO 1MHZ, POMIAROW POWINNO BYC 1000
#POMIAR NAPIECIA DLA KAZDEJ Z CZESTOTLIWOSCI ABY ZAOBSERWOWAC ZMIANY WZMOCNIENIA WRAZ ZE WZROSTEM CZESTOTLIWOSCI


#Komendy dla MSO

#polaczenie przez usb
#
*CLS
*IDN?
*RST
:SELect:CH2 1
:AUTOSet EXECute 
MEASUrement:IMMed:TYPe? PK2PK;UNITS "V";SOURCE1 CH1 *ESR?  #strona 276 w PH #concentrating na strojnie 20
MEASUrement:IMMed:VALue? #chyba trzeba to wyslac jako kolejna komende
#byc moze trzeba bedzie komende do znalezienia trigger levlu


#Komendy dla generatora

*OPC?
*WAI
*CLS

WAVE SQUARE
FREQ 10000
AMPUNIT VPP
AMPL 1
OUTPUT ON



"""

