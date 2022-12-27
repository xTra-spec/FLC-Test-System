##################################### Linearity #########################################
start_vpp = 0
step_vpp = 1
stop_vpp = 20

gen_axis = []

for i in range(stop_vpp):
    start_vpp += step_vpp
    gen_axis.append(start_vpp)
    #start_vpp = int(start_vpp)

#print(gen_axis)

gain = 10
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