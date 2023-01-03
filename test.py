vpp = 0.1

def gen_settings(amplitude, frequency):
    print(('WAVE SQUARE;AMPUNIT VPP;AMPL '+amplitude+';FREQ '+frequency+';OUTPUT ON'))
    return

#gen_settings(str(vpp), '10000')
gen_settings(vpp, '10000')