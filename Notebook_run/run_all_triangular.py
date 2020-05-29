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
posdur = sys.argv[arg]; arg=arg+1
posamp = sys.argv[arg]; arg=arg+1
possamp = sys.argv[arg]; arg=arg+1
ld = sys.argv[arg]; arg=arg+1
diam = sys.argv[arg]; arg=arg+1
gnap = sys.argv[arg]; arg=arg+1
gcal = sys.argv[arg]; arg=arg+1
gks = sys.argv[arg]; arg=arg+1   


gama = float(gama)
delay = float(delay)
predur = float(predur)
posdur = float(posdur)
posamp = float(posamp)
possamp = float(possamp)
ld = float(ld)
diam = float(diam)
gnap = float(gnap)
gcal = float(gcal)
gks = float(gks)   


soma = nrn.h.Section()
dend = nrn.h.Section()

i_vec = nrn.h.Vector()
v_vec = nrn.h.Vector()             # Membrane potential vector
v_vecs = nrn.h.Vector()
t_vec = nrn.h.Vector()

dend.connect(soma, 0, 1)
# soma mechanisms
soma.insert('napp')
# dendrite mechanisms
dend.insert('caL')


stimtriang = nrn.h.iTriang(0.5, sec=soma)


#inject current in the soma section
stimtriang.delay = delay
stimtriang.predur = predur
stimtriang.posdur = posdur
stimtriang.posamp = posamp
stimtriang.possamp = possamp


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
i_vec.record(stimtriang._ref_i)
t_vec = nrn.h.Vector()             
t_vec.record(nrn.h._ref_t)

icaL_vec= nrn.h.Vector()
icaL_vec.record(dend(0.5)._ref_icaL)

# run the simulation
nrn.h.load_file("stdrun.hoc")
#h.init()
nrn.h.dt = 0.001
nrn.h.tstop = delay + predur + posdur 
nrn.h.v_init = 0
nrn.h.run()

freq = []
nparray_volt = np.array(v_vec.to_python())
nparray_time = np.array(t_vec.to_python())
nparray_current = np.array(i_vec.to_python())
maxima = argrelextrema(nparray_volt, np.greater)
spikes = [j for j in maxima[0] if nparray_volt[j] >= 65] 
maxima_volt = nparray_volt[spikes]
maxima_time = nparray_time[spikes]
maxima_current = nparray_current[spikes]


if len(spikes) > 1:
    maxima_interval = np.diff(maxima_time)
    freq = (1000.0/(maxima_interval))

# plot the results
import matplotlib
from matplotlib import pyplot
matplotlib.rc('font', size = 8)
pyplot.rcParams.update({'font.size': 8})
pyplot.rc('xtick', labelsize=15)
pyplot.rc('ytick', labelsize=15)
pyplot.rc('axes', labelsize=15)


f, axarr = pyplot.subplots(4, figsize=(7, 8))

axarr[0].plot(maxima_current[1:],freq, 'black')
axarr[1].plot(maxima_time[1:], freq,'black', linewidth=1,label='freq (Hz)')
axarr[2].plot(t_vec, v_vec,'black', linewidth=1, label='potential (mV) - %s type' % mutype)
axarr[3].plot(t_vec, i_vec, 'black', label='applied current (nA)', linewidth=2.0) 


axarr[1].set_xlim([0,15020])

axarr[0].set_ylabel('Firing rate (Hz)',fontsize=15)
axarr[1].set_ylabel('Firing rate (Hz)', fontsize = 15)
axarr[2].set_ylabel('Vs (mV)', fontsize = 15)
axarr[3].set_ylabel('Current (nA)', fontsize = 15)

axarr[0].set_xlabel('Current (nA)',fontsize=15)
axarr[3].set_xlabel('Time (ms)', fontsize = 15)


axarr[0].grid(b=True)
axarr[1].grid(b=True)
axarr[2].grid(b=True)
axarr[3].grid(b=True)
axarr[0].tick_params(labelsize=15)
axarr[1].tick_params(labelsize=15)
axarr[2].tick_params(labelsize=15)
axarr[3].tick_params(labelsize=15)
pyplot.tight_layout(rect=(0,0,1,.98))

frequency = freq[-1]-freq[0]
current=maxima_current[-1]-maxima_current[0]
spikes=len(spikes)
import pandas as pd
df2 = pd.DataFrame({'delta_f':frequency,
                    'delta_i':current,
                    'spikes':[spikes]})
df2.to_csv('triangular_injection_results.csv', index=False)
pyplot.savefig('triangular_injection.png')