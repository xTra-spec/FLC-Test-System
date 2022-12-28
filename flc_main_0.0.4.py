"""
1. Mozliwość wyboru modelu jednostki, zaleznie od wyboru, zostaną dobrane odpowiednie nastawy generatora i wyniki PASS/FAIL (specyficzne informacje nt jednostki w oddzielnym pliku)
2. Uzytkownik moze wpisac numer seryjny, data to lokalny czas komputera
3. Sprzęt: Oscyloskop Teka, Generator, PC
4. Testy: Wykres liniowości wzmacniacza, pomiar BW, SLEW RATE
5. Check lista, infomacje jaki ustawić Rise/Fall time dla danej jednostki, nastawy genratora są wybierane automatycznie, program pokaze czy miesci sie w limitach
6. Automatyczne tworzenie certyfikatu kalibracji z wykresem liniowosci, zapis do pliku

"""
"""
print("FLC Testy system v0.0.4")

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

##################################### Linearity #########################################
"""
import pyvisa
import time
import matplotlib.pyplot as plt
import numpy as np

rm = pyvisa.ResourceManager()

gen = rm.open_resource('ASRL4::INSTR')
mso = rm.open_resource('USB0::0x0699::0x0423::C030847::INSTR')

def idn(): 
    print(mso.query('*IDN?'))
    print(gen.query('*IDN?'))
    return

def gen_reset():                       
    gen.write('*RST;*CLS')
    return

def mso_reset():
    mso.write('*RST;*CLS')
    return

def mso_channel_selection(channel):
    mso.write('SELect:'+channel+'1')
    return

def gen_settings(amplitude, frequency):
    gen.write('WAVE SQUARE;AMPUNIT VPP;AMPL'+amplitude+';FREQ'+frequency+';OUTPUT ON')
    return

def mso_measurement():
    mso.query('MEASUrement:IMMed:VALue?')
    return
def mso_autoset():
    mso.write('AUTOSet EXECute')
    return
def mso_measurement_type():
    mso.write('MEASUrement:IMMed:TYPe PK2PK')
    return

def mso_measurement_source(channel):
    mso.write('MEASUrement:IMMed:SOURCE1'+channel)
    return

vpp = 0.1
step_vpp = 0.1
measured_gen_vpp = []
measured_amp_vpp = []

gen_reset()
gen_settings(vpp, '10000')
mso_reset()
mso_channel_selection('CH1')
mso_channel_selection('CH2')
mso_measurement_type()
mso_autoset()

while vpp < 4: # sweep vpp to 5Vpp
    gen_settings(vpp,'10000')
    #gen.write("AMPL " + str(vpp))
    if vpp < 4:
        mso_measurement_source('CH1')
        x = mso_measurement() #channel 1
        x = float(x)
        measured_gen_vpp.append(x)
        print(x)
        mso_measurement_source('CH2')
        o = mso_measurement()
        o = float(o)
        measured_amp_vpp.append(o)
        print(o)

    vpp += step_vpp
     
xpoints = np.array([measured_amp_vpp])
ypoints = np.array([measured_gen_vpp])

plt.plot(measured_amp_vpp, measured_gen_vpp)
plt.title("Amplification Linearity")
plt.xlabel("Voltage Output (Vpp)")
plt.ylabel("Voltage Input (Vpp)")
plt.grid()
plt.show()

gen_reset()
mso_reset()

"""
##################################### Bandwith #########################################

import matplotlib.pyplot as plt
import numpy as np

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

"""
*IDN?
*RST
:SELect:CH2 1
:AUTOSet EXECute
MEASUrement:IMMed:TYPe PK2PK;SOURCE1 CH3\n 
MEASUrement:IMMed:TYPe PK2PK;UNITS "V";SOURCE1 CH1\n *ESR?  #strona 276 w PH #concentrating na strojnie 20
MEASUREMENT:IMMED:TYPE PERIOD;UNITS "s";SOURCE1 CH1;SOURCE2
MEASUrement:IMMed:VALue? #chyba trzeba to wyslac jako kolejna komende
#byc moze trzeba bedzie komende do znalezienia trigger levlu
MEASUrement:IMMed?\n

MEASUrement:IMMed:TYPe PK2PK; SOURCE1 CH1\n 

#Komendy dla generatora

*OPC?
*WAI
*CLS

WAVE SQUARE
FREQ 10000
AMPUNIT VPP
AMPL 1
OUTPUT ON

mso.write('SELect:CH2 1')
mso.write('MEASUrement:IMMed:SOURCE1 CH2')
mso.write('AUTOSet EXECute')
time.sleep(2.5)
mso.write('MEASUrement:IMMed:TYPe PK2PK')
time.sleep(2.5)

print(mso.query('MEASUrement:IMMed:VALue?'))

"""

