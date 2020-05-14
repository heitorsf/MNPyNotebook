from itertools import chain
import os
if 'DISPLAY' in os.environ:
    del os.environ['DISPLAY']
import sys
sys.path.insert(0, '/usr/local/nrn/lib/python/')
import neuron as nrn
import mu_type
import numpy as np
from scipy.signal import argrelextrema
from ipywidgets import FloatSlider
from scipy.optimize import leastsq
from IPython.display import display, Image
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
        
        import subprocess
        #print('start run_all_pulse.py')
        #os_out=os.system('ipython run_all_pulse.py --'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.meddur)+' '+str(self.posdur)+' '+str(self.preamp)+' '+str(self.posamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))
      
    
        #if os_out !=0:
        #    print('ERRO no os.system',os_out)
        #print('rodei run_all.py')
        
        subprocess.check_output('ipython run_all_pulse.py --'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.meddur)+' '+str(self.posdur)+' '+str(self.preamp)+' '+str(self.posamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks),stderr=subprocess.STDOUT, shell=True)
        try:
            print(stderr)
        except:
            pass
        #    print('ok')
        #print('finish run_all_pulse.py')
        
        display(Image(filename='pulse_injection.png'))
    
    def view_pulse(self,mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks):
        self.delay = delay                 
        self.predur = predur
        self.meddur = meddur
        self.posdur = posdur
        self.preamp = preamp
        self.posamp = posamp
        self.ld = ld
        self.diam = diam
        self.gnap = gnap*1e-3
        self.gcal = gcal*1e-3
        self.gks= gks*1e-3
        self.mutype = mutype
        self.params_pulse()
        

    def params_triangular(self):

        #print('start run_all_triangular.py')
        os_out=os.system('ipython run_all_triangular.py'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.posdur)+' '+str(self.posamp)+' '+str(self.possamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))
      
        if os_out !=0:
            print('ERRO no os.system',os_out)
        #print('finish run_all_triangular.py')
        
        display(Image(filename='triangular_injection.png'))
     
    def view_triangular(self,mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks):
        self.delay = delay                 
        self.predur = predur
        self.posdur = posdur
        self.gama = gama
        self.posamp = posamp
        self.possamp = possamp
        self.ld = ld
        self.diam = diam
        self.gnap = gnap*1e-3
        self.gcal = gcal*1e-3
        self.gks= gks*1e-3
        self.mutype = mutype
        self.params_triangular()