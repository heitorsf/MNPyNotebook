import sys
import neuron as nrn
import mu_type
import numpy as np
from scipy.signal import argrelextrema
from matplotlib import pyplot
      

arg=1
mutype = sys.argv[arg]; arg=arg+1
gama = sys.argv[arg]; arg=arg+1
delay = sys.argv[arg]; arg=arg+1
predur = sys.argv[arg]; arg=arg+1
meddur = sys.argv[arg]; arg=arg+1
posdur = sys.argv[arg]; arg=arg+1
preamp = sys.argv[arg]; arg=arg+1
posamp = sys.argv[arg]; arg=arg+1
ld = sys.argv[arg]; arg=arg+1
diam = sys.argv[arg]; arg=arg+1
gnap = sys.argv[arg]; arg=arg+1
gcal = sys.argv[arg]; arg=arg+1
gks = sys.argv[arg]; arg=arg+1   


gama = float(gama)
delay = float(delay)
predur = float(predur)
meddur = float(meddur)
posdur = float(posdur)
preamp = float(preamp)
posamp = float(posamp)
ld = float(ld)
diam = float(diam)
gnap = float(gnap)
gcal = float(gcal)
gks = float(gks)   


soma = nrn.h.Section()
dend = nrn.h.Section()

i_vec = nrn.h.Vector()
v_vec = nrn.h.Vector()           
v_vecs = nrn.h.Vector()
t_vec = nrn.h.Vector()

dend.connect(soma, 0, 1)
# soma mechanisms
soma.insert('napp')
# dendrite mechanisms
dend.insert('caL')

stimtest = nrn.h.iTest(0.5, sec=soma)


#inject current in the soma section
stimtest.delay = delay
stimtest.predur = predur
stimtest.meddur = meddur
stimtest.posdur = posdur
stimtest.preamp = preamp
stimtest.posamp = posamp


if mutype == 'S':
    mu_type.mus(soma,dend)
elif mutype == 'FR':
    mu_type.mufr(soma,dend)
elif mutype == 'FF':
    mu_type.muff(soma,dend)
else:
    raise ValueError("invalid mutype")


soma.gnapbar_napp = gnap
dend.gcaLbar_caL = gcal
soma.gksbar_napp = gks
dend.L = ld
dend.diam = diam
dend.gama_caL = gama

v_vec.record(soma(0.5)._ref_v)
v_vecs.record(dend(0.5)._ref_v)
i_vec.record(stimtest._ref_i)
t_vec = nrn.h.Vector()             
t_vec.record(nrn.h._ref_t)

# run the simulation
nrn.h.load_file("stdrun.hoc")
nrn.h.init()
nrn.h.dt = 0.01
nrn.h.tstop = delay + predur + meddur + posdur + 1000
nrn.h.v_init = 0
nrn.h.run()

freq = []
nparray_volt = np.array(v_vec.to_python())
nparray_volts = np.array(v_vecs.to_python())
nparray_time = np.array(t_vec.to_python())
nparray_current = np.array(i_vec.to_python())
maxima = argrelextrema(nparray_volt, np.greater)
spikes = [j for j in maxima[0] if nparray_volt[j] >= 60]
pike = [i for i in maxima[0] if nparray_volt[i] >= 0.6]
maxima_volt = nparray_volt[spikes]
maxima_time = nparray_time[spikes]
maxima_current = nparray_current[spikes]
maxima_times = nparray_time[pike]
maxima_volts = nparray_volt[pike]
minimum = min(nparray_volt)

if len(spikes) > 1:
    maxima_interval = np.diff(maxima_time)
    freq = (1000.0/(maxima_interval))

elif len(spikes) == 1:
    print (maxima_volt)
    print (maxima_time)

else:
    print (maxima_volts)
    print (maxima_volts*0.63)
    print (maxima_times)
    print(minimum)


pyplot.rcParams.update({'font.size': 15})
pyplot.rc('xtick', labelsize=15)
pyplot.rc('ytick', labelsize=15)
pyplot.rc('axes', labelsize=15)

f, axarr = pyplot.subplots(3, sharex=True,figsize=(7, 7))


axarr[0].plot(maxima_time[1:], freq,'black', linewidth=1,label='freq (Hz)')
axarr[0].set_ylabel('Firing Rate (Hz)',rotation=90)
axarr[0].grid()

axarr[1].plot(t_vec, v_vec,'black', linewidth=1, label='potential (mV) - %s type' % mutype)
axarr[1].set_ylabel('Vs (mV)',rotation=90)
axarr[1].grid()

axarr[2].plot(t_vec, i_vec, 'black', label='applied current (nA)', linewidth=2.0)
axarr[2].set_ylabel('Current (nA)',rotation=90)
axarr[2].grid()

pyplot.xlabel('Time (ms)')
pyplot.tight_layout(0.1)

spikes=len(spikes)
import pandas as pd
df2 = pd.DataFrame({'frequency':np.mean(freq),
                    'spikes':[spikes]})
df2.to_csv('pulse_injection_results.csv', index=False)
pyplot.savefig('pulse_injection.png')