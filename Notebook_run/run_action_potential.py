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
dur = sys.argv[arg]; arg=arg+1
amp = sys.argv[arg]; arg=arg+1
ld = sys.argv[arg]; arg=arg+1
diam = sys.argv[arg]; arg=arg+1
gnap = sys.argv[arg]; arg=arg+1
gcal = sys.argv[arg]; arg=arg+1
gks = sys.argv[arg]; arg=arg+1   


gama = float(gama)
delay = float(delay)
dur = float(dur)
amp = float(amp)
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
icaL_vec= nrn.h.Vector()
ina_vec = nrn.h.Vector()
inaf_vec = nrn.h.Vector()
inap_vec = nrn.h.Vector()
ik_vec = nrn.h.Vector()
iks_vec = nrn.h.Vector()
ikf_vec = nrn.h.Vector()
gks_vec = nrn.h.Vector()
gkf_vec = nrn.h.Vector()
gna_vec = nrn.h.Vector()
gnaf_vec = nrn.h.Vector()
gnap_vec = nrn.h.Vector()
gcal_vec = nrn.h.Vector()


dend.connect(soma, 0, 1)
# soma mechanisms
soma.insert('napp')
soma.insert('Constant')
# dendrite mechanisms
dend.insert('caL')
dend.insert('Constant')

IClamp = nrn.h.IClamp(0.5, sec=soma)


#inject current in the soma section
IClamp.delay = delay
IClamp.amp = amp
IClamp.dur = dur


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
i_vec.record(IClamp._ref_i)
t_vec = nrn.h.Vector()             
t_vec.record(nrn.h._ref_t)


icaL_vec.record(dend(0.5)._ref_icaL)
ina_vec.record(soma(0.5)._ref_ina)
inaf_vec.record(soma(0.5)._ref_inaf_napp)
inap_vec.record(soma(0.5)._ref_inap_napp)
#ik_vec.record(soma(0.5)._ref_ik_napp)
iks_vec.record(soma(0.5)._ref_iks_napp)
ikf_vec.record(soma(0.5)._ref_ikf_napp)

gcal_vec.record(dend(0.5)._ref_gcaL_caL)
gks_vec.record(soma(0.5)._ref_gks_napp)
gkf_vec.record(soma(0.5)._ref_gkf_napp)
gna_vec.record(soma(0.5)._ref_gna_napp)
gnap_vec.record(soma(0.5)._ref_gnap_napp)


# run the simulation
nrn.h.load_file("stdrun.hoc")
nrn.h.init(1)
nrn.h.finitialize(0)
nrn.h.v_init = 0.000
soma.ic_Constant = -(soma.ina+soma.ik+soma.il_napp)
dend.ic_Constant = -(dend.icaL_caL+dend.il_caL)
nrn.h.dt = 0.01
nrn.h.tstop = delay + dur + 20
nrn.h.run()

freq = []
nparray_volt = np.array(v_vec.to_python())
nparray_volts = np.array(v_vecs.to_python())
nparray_time = np.array(t_vec.to_python())
gcal_vec = np.array(gcal_vec.to_python())
gks_vec = np.array(gks_vec.to_python())
gkf_vec = np.array(gkf_vec.to_python())
gna_vec = np.array(gna_vec.to_python())
gnap_vec = np.array(gnap_vec.to_python())
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


f, ((axarr0,axarr1,axarr4),(axarr2,axarr3,axarr5)) = pyplot.subplots(ncols=3, nrows=2,sharex=True,figsize=(18, 18))


axarr0.plot(t_vec, i_vec, 'black', label='applied current (nA)', linewidth=2.0)
axarr0.set_ylabel('Current (nA)',rotation=90)
axarr0.set_xlim(18,40)

axarr1.plot(t_vec, nparray_volt,'black', linewidth=1, label='potential (mV) - %s type' % mutype)
axarr1.set_ylabel('Vs (mV)',rotation=90)
axarr1.set_xlim(18,40)

axarr2.plot(t_vec, gna_vec*1e3, linewidth=1,label=u'gNa ($mS/cm^2$)')
axarr2.plot(t_vec, gnap_vec*1e3, linewidth=1,label=u'gNap ($mS/cm^2$)')
axarr2.plot(t_vec, gks_vec*1e3, linewidth=1,label=u'gKs ($mS/cm^2$)')
axarr2.plot(t_vec, gkf_vec*1e3, linewidth=1,label=u'gKf ($mS/cm^2$)')
axarr2.set_ylabel(u'Ionic Conductance ($mS/cm^2$)',rotation=90)
axarr2.set_xlim(18,40)
axarr2.legend(loc='best')
axarr2.set_xlabel('Time (ms)')

axarr3.plot(t_vec, inaf_vec, linewidth=1,label=u'INa ($mA/cm^2$)')
axarr3.plot(t_vec, inap_vec, linewidth=1,label=u'INap ($mA/cm^2$)')
axarr3.plot(t_vec, iks_vec, linewidth=1,label=u'IKs ($mA/cm^2$)')
axarr3.plot(t_vec, ikf_vec, linewidth=1,label=u'IKf ($mA/cm^2$)')
axarr3.set_ylabel(u'Ionic Current ($mA/cm^2$)',rotation=90)
axarr3.set_xlim(18,40)
axarr3.legend(loc='best')
axarr3.set_xlabel('Time (ms)')

axarr4.plot(t_vec, nparray_volts,'black', linewidth=1, label='potential (mV) - %s type' % mutype)
axarr4.set_ylabel('Vd (mV)',rotation=90)
axarr4.set_xlim(18,40)

axarr5.set_xlabel('Time(ms)')
axarr5.set_ylabel('mA/cm²', color = 'b')

for t1 in axarr5.get_yticklabels():
    t1.set_color('b')
    
ax2 = axarr5.twinx()

for t1 in ax2.get_yticklabels():
    t1.set_color('r')


axarr5.plot(t_vec, icaL_vec, linewidth=1,label=u'ICaL ($mA/cm^2$)',color='b')
axarr5.set_xlabel('Time (ms)')
axarr5.set_ylabel(u'Ionic Current ($mA/cm^2$)',rotation=90,color='b')
axarr5.legend (loc = 1) #best

ax2.plot(t_vec, gcal_vec*1e3, linewidth=1,label=u'gCaL ($mS/cm^2$)',color='r')
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel(u'Ionic Conductance ($mS/cm^2$)',rotation=90,color='r')
ax2.legend (loc = 'center')#4


pyplot.xlabel('Time(ms)')


axarr0.grid()
axarr1.grid()
axarr2.grid()
axarr3.grid()
axarr4.grid()
axarr5.grid()


pyplot.tight_layout(0.1)

spikes=len(spikes)
import pandas as pd
df2 = pd.DataFrame({'frequency':np.mean(freq),
                    'spikes':[spikes]})
df2.to_csv('action_potential_results.csv', index=False)
pyplot.savefig('action_potential.png')