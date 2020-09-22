import os
if 'DISPLAY' in os.environ:
    del os.environ['DISPLAY']
import sys
sys.path.insert(0, '/usr/local/nrn/lib/python/')
from IPython.display import display, Image, clear_output


class params_init(object):
    
    def __init__(self):
        self.delay = 100   
        self.dur = 0.5
        self.amp = 45.
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

    def params_pulse(self):
        
        import subprocess
        #os_out=os.system('ipython run_all_pulse.py --'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.meddur)+' '+str(self.posdur)+' '+str(self.preamp)+' '+str(self.posamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))
      
    
        #if os_out !=0:
        #    print('ERRO no os.system',os_out)
        
        subprocess.check_output('ipython run_all_pulse.py --'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.meddur)+' '+str(self.posdur)+' '+str(self.preamp)+' '+str(self.posamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks),stderr=subprocess.STDOUT, shell=True)
        try:
            print(stderr)
        except:
            pass
        
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


        os_out=os.system('ipython run_all_triangular.py'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.posdur)+' '+str(self.posamp)+' '+str(self.possamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))
      
        if os_out !=0:
            print('ERRO no os.system',os_out)
        
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
        
      
    def params_action_potential(self):

        
        import subprocess
        
        subprocess.check_output('ipython run_action_potential.py'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.dur)+' '+str(self.amp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks),stderr=subprocess.STDOUT, shell=True)
        try:
            print(stderr)
        except:
            pass
        
        display(Image(filename='action_potential.png'))
     
    def view_action_potential(self,mutype,gama,delay,dur,amp,ld,diam,gnap,gcal,gks):
        self.delay = delay                 
        self.dur = dur
        self.gama = gama
        self.amp = amp
        self.ld = ld
        self.diam = diam
        self.gnap = gnap*1e-3
        self.gcal = gcal*1e-3
        self.gks= gks*1e-3
        self.mutype = mutype
        self.params_action_potential()
        
    def params_inject_current(mode):
        if mode == 'pulse':
                    
            os_out=os.system('ipython run_all_pulse.py --'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.meddur)+' '+str(self.posdur)+' '+str(self.preamp)+' '+str(self.posamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))

            if os_out !=0:
                print('ERRO no os.system',os_out)

            display(Image(filename='pulse_injection.png'))
            
        if mode == 'triangular':
           
            os_out=os.system('ipython run_all_triangular.py'+' '+str(self.mutype)+' '+str(self.gama)+' '+str(self.delay)+' ' +str(self.predur)+' '+str(self.posdur)+' '+str(self.posamp)+' '+str(self.possamp)+' '+str(self.ld)+' '+str(self.diam)+' '+str(self.gnap)+' '+str(self.gcal)+' '+str(self.gks))

            if os_out !=0:
                print('ERRO no os.system',os_out)

            display(Image(filename='triangular_injection.png'))
     
    def view_current(self,mode):
        if mode == 'pulse':
            def view_current(self,mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks):
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
            
        elif mode =='triangular':
              def view_current(self,mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks):
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
        else: 
            print("Sintaxe error: this current doesn't exist")
     
        