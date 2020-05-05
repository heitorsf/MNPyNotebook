from itertools import chain
from neuron import *
from mu_type import *
import numpy as np
from scipy.signal import argrelextrema
from ipywidgets import FloatSlider
from scipy.optimize import leastsq
from IPython.display import display
from matplotlib import pyplot

from IPython.display import clear_output

class params_init(object):
    
    def __init__(self):
        self.delay = 100                 
        self.predur = 3000 
        self.meddur = 3000
        self.posdur = 12250
        self.preamp = 10
        self.posamp = 12
        self.possamp = 27
        self.ld = 6150
        self.diam = 52
        self.gnap = 0.00052
        self.gcal = 0.00001
        self.gks= 0.018
        self.gama = 1.
        self.mutype = 'S'
        #self.config={}

    def params_pulse(self):

        soma = h.Section()
        dend = h.Section()

        i_vec = h.Vector()
        v_vec = h.Vector()             # Membrane potential vector
        v_vecs = h.Vector()
        t_vec = h.Vector()

        dend.connect(soma, 0, 1)
        # soma mechanisms
        soma.insert('napp')
        ## dendrite mechanisms
        dend.insert('caL')

        stimtest = h.iTest(0.5, sec=soma)


        #inject current in the soma section
        stimtest.delay = self.delay
        stimtest.predur = self.predur
        stimtest.meddur = self.meddur
        stimtest.posdur = self.posdur
        stimtest.preamp = self.preamp
        stimtest.posamp = self.posamp

        
        if self.mutype == "S":
            mus(soma,dend)
        elif self.mutype == "FR":
            mufr(soma,dend)
        elif self.mutype == "FF":
            muff(soma,dend)
        #print(self.mutype)

        soma.gnapbar_napp = self.gnap
        dend.gcaLbar_caL = self.gcal
        soma.gksbar_napp = self.gks
        dend.L = self.ld
        dend.diam = self.diam
        dend.gama_caL = self.gama

        v_vec.record(soma(0.5)._ref_v)
        v_vecs.record(dend(0.5)._ref_v)
        i_vec.record(stimtest._ref_i)
        t_vec = h.Vector()             # Time stamp vector
        t_vec.record(h._ref_t)

        # run the simulation
        h.load_file("stdrun.hoc")
        #h.init()
        h.dt = 0.01
        h.tstop = 7000
        h.v_init = 0
        h.run()

        freq = []
        nparray_volt = np.array(v_vec.to_python())
        nparray_volts = np.array(v_vecs.to_python())
        nparray_time = np.array(t_vec.to_python())
        nparray_current = np.array(i_vec.to_python())
        maxima = argrelextrema(nparray_volt, np.greater)
        spikes = [j for j in maxima[0] if nparray_volt[j] >= 60] # clean maxima "mistakes"
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

            print ('i= %f nA, %d spikes' % (self.preamp,len(spikes)))
        #    print (maxima_volt)
        #    print (maxima_time)
        #    print (maxima_interval)
        #    print ('freq = %f Hz' % freq)

        elif len(spikes) == 1:
            print (maxima_volt)
            print (maxima_time)
            print ('apenas um PA, frequencia = ?')

        else:
            print ('pulso sublimiar')
            print (maxima_volts)
            print (maxima_volts*0.63)
            print (maxima_times)
            print(minimum)


        f, axarr = pyplot.subplots(4, sharex=True,figsize=(7, 7))

        axarr[3].plot(t_vec, i_vec, 'black', label='applied current (nA)', linewidth=2.0)
        axarr[2].plot(t_vec, v_vec,'black', linewidth=1, label='potential (mV) - %s type' % self.mutype)
        axarr[0].plot(maxima_time[1:], freq,'black', linewidth=1,label='freq (Hz)')
        axarr[1].plot(t_vec, v_vecs,'black', linewidth=1, label='dend potential (mV) - %s type' % self.mutype)

        clear_output()

        pyplot.rcParams.update({'font.size': 8})
        pyplot.rc('xtick', labelsize=10)
        pyplot.rc('ytick', labelsize=10)
        pyplot.rc('axes', labelsize=10)

        #axarr[3].yaxis.set_label_position("right")


        axarr[3].set_ylim([-12,12])
        axarr[0].grid()
        axarr[1].grid()
        axarr[2].grid()
        axarr[3].grid()

        axarr[3].set_ylabel('Injected Current(nA)',rotation=90)
        axarr[2].set_ylabel('Soma Potential(mV)',rotation=90)
        axarr[0].set_ylabel('Firing Rate(Hz)',rotation=90)
        axarr[1].set_ylabel('Dendrite Potential(mV)',rotation=90)

        pyplot.xlabel('Time')
        axes = pyplot.gca()
        axes.set_xlim([0,7000])

        pyplot.tight_layout()
        pyplot.show()

        return self.mutype,self.gama,self.delay,self.predur,self.meddur,self.posdur,self.preamp,self.posamp,self.ld,self.diam,self.gnap,self.gcal,self.gks
    
    def view_pulse(self,mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks):
        self.delay = delay                 
        self.predur = predur
        self.meddur = meddur
        self.posdur = posdur
        self.preamp = preamp
        self.posamp = posamp
        self.ld = ld
        self.diam = diam
        self.gnap = gnap
        self.gcal = gcal
        self.gks= gks
        self.mutype = mutype
        self.params_pulse()
        

    def params_triangular(self):

        soma = h.Section()
        dend = h.Section()

        i_vec = h.Vector()
        v_vec = h.Vector()             # Membrane potential vector
        v_vecs = h.Vector()
        t_vec = h.Vector()

        dend.connect(soma, 0, 1)
        # soma mechanisms
        soma.insert('napp')
        ## dendrite mechanisms
        dend.insert('caL')


        stimtriang = h.iTriang(0.5, sec=soma)

   
        #inject current in the soma section
        stimtriang.delay = self.delay
        stimtriang.predur = self.predur
        stimtriang.posdur = self.posdur
        stimtriang.posamp = self.posamp
        stimtriang.possamp = self.possamp

        #self.mutype = mutype

        if self.mutype == 'S':
            mus(soma,dend)
        elif self.mutype == 'FR':
            mufr(soma,dend)
        elif self.mutype == 'FF':
            muff(soma,dend)
        #print(self.mutype)

        soma.gnapbar_napp = self.gnap
        dend.gcaLbar_caL = self.gcal
        soma.gksbar_napp = self.gks
        dend.L = self.ld
        dend.diam = self.diam
        dend.gama_caL = self.gama
     

        v_vec.record(soma(0.5)._ref_v)
        i_vec.record(stimtriang._ref_i)
        t_vec = h.Vector()             # Time stamp vector
        t_vec.record(h._ref_t)

        icaL_vec= h.Vector()
        icaL_vec.record(dend(0.5)._ref_icaL)

        # run the simulation
        h.load_file("stdrun.hoc")
        #h.init()
        h.dt = 0.001
        h.tstop = self.delay + self.predur + self.posdur 
        h.v_init = 0
        h.run()

        freq = []
        nparray_volt = np.array(v_vec.to_python())
        nparray_time = np.array(t_vec.to_python())
        nparray_current = np.array(i_vec.to_python())
        maxima = argrelextrema(nparray_volt, np.greater)
        spikes = [j for j in maxima[0] if nparray_volt[j] >= 65] # clean maxima "mistakes"
        maxima_volt = nparray_volt[spikes]
        maxima_time = nparray_time[spikes]
        maxima_current = nparray_current[spikes]
        #print('last_current',np.min(nparray_current[spikes]))
        #print('first_current',maxima_current[0])



        if len(spikes) > 1:
            maxima_interval = np.diff(maxima_time)
            freq = (1000.0/(maxima_interval))
            #freq = (1000.0/np.average (maxima_interval))
            #print ('freq = %f Hz' % freq)

        # plot the results
        import matplotlib
        from matplotlib import pyplot
        matplotlib.rc('font', size = 8)
        pyplot.rcParams.update({'font.size': 8})
        pyplot.rc('xtick', labelsize=15)
        pyplot.rc('ytick', labelsize=15)
        pyplot.rc('axes', labelsize=15)

        f, axarr = pyplot.subplots(3, sharex=True,figsize=(7, 7))
        #axarr[3].plot(maxima_current[1:],freq, 'black')
        axarr[2].plot(t_vec, i_vec, 'black', label='applied current (nA)', linewidth=2.0)
        axarr[1].plot(t_vec, v_vec,'black', linewidth=1, label='potential (mV) - %s type' % self.mutype)
        axarr[0].plot(maxima_time[1:], freq,'black', linewidth=1,label='freq (Hz)')
        #axarr[3].set_ylabel('Firing rate (Hz)',fontsize=15)
        axarr[2].set_ylabel('Current (nA)', fontsize = 15)
        axarr[1].set_ylabel('Vs (mV)', fontsize = 15)
        axarr[0].set_ylabel('Firing rate (Hz)', fontsize = 15)
        axarr[2].set_xlabel('Time (ms)', fontsize = 15)
        #axarr[3].set_xlabel('Current (nA)',fontsize=15)
        axes = pyplot.gca()
        #axes.set_xlim([0,10020])
        #axarr[3].set_ylim([-20,20])
        axarr[0].grid()
        axarr[1].grid()
        axarr[2].grid()
        #axarr[3].grid()
        axarr[0].tick_params(labelsize=15)
        axarr[1].tick_params(labelsize=15)
        axarr[2].tick_params(labelsize=15)
        #axarr[3].tick_params(labelsize=15)
        pyplot.tight_layout(0.1)

        pyplot.figure(figsize=(8, 8))
        pyplot.plot(maxima_current[1:],freq, 'black')
        pyplot.title('f-I')
        pyplot.xlabel('Current (nA)')
        pyplot.ylabel('Firing rate (Hz)')
        pyplot.show()

        return self.mutype,self.gama,self.delay,self.predur,self.posdur,self.posamp,self.possamp,self.ld,self.diam,self.gnap,self.gcal,self.gks
    
    def view_triangular(self,mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks):
        self.delay = delay                 
        self.predur = predur
        self.posdur = posdur
        self.gama = gama
        #self.preamp = preamp
        self.posamp = posamp
        self.possamp = possamp
        self.ld = ld
        self.diam = diam
        self.gnap = gnap
        self.gcal = gcal
        self.gks= gks
        self.mutype = mutype
        self.params_triangular()