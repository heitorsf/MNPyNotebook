import numpy as np
from IPython.display import display
from matplotlib import pyplot

import ipywidgets as widgets
from ipywidgets import FloatSlider, Dropdown, Layout, HBox, RadioButtons

def widget_interact_manual_current(pulse,triangular):
    if pulse == True:
        style = {'description_width': 'initial'}
        gks= widgets.FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                        description='Slow potassium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '500px'), style = style)

        gcal= widgets.FloatSlider(value = 0.00001, min = 0.00001, max = 0.00062,
                        description='Calcium type-L conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '500px'), style = style)

        gnap= widgets.FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                        description='Persistent sodium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '500px'), style = style)

        mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                      layout = Layout(width = '200px'),continuous_update = True,
                      description = 'Motor Neuron Type:', style = style)

        gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                      layout = Layout(width = '200px'),continuous_update = True,
                      description = 'Monoamnergic Drive:', style = style)

        delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                      layout = Layout(width = '200px'),continuous_update = True,
                      description = 'Injected current delay [$ms$]:', style = style)

        predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                        description='Depolarizing current pulse duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                        description='Time between current pulses [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                        description='Hyperpolarizing current pulse duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        preamp= widgets.FloatSlider(value = 10, min = -30, max = 50,
                        description='Depolarizing current pulse amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        posamp= widgets.FloatSlider(value = -10, min = -30, max = 50,
                        description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        ld= widgets.FloatSlider(value = 6150, min = 1000, max = 25000,
                        description='Dendrite Lenght[$mm$]:', 
                        layout = Layout(width= '400px'), style = style)

        diam = widgets.FloatSlider(value = 50, min = 10, max = 300,
                        description='Dendrite Diameter[$um$]:', 
                        layout = Layout(width= '400px'), style = style)
        return [mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks]
    
    if triangular == True:
        style = {'description_width': 'initial'}
        gks= FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                        description='Slow potassium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '450px'), style = style)

        gcal= FloatSlider(value = 0.00001, min = 0.000001, max = 0.000062,
                        description='L-type calcium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        gnap= FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                        description='Persistent sodium conductance [$mS/cm^2$]:', 
                        layout = Layout(width= '400px'), style = style)

        mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Motor neuron type:', style = style)

        gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Monoaminergic drive:', style = style)

        delay = Dropdown(options = range(0,300,10), value = 20,
                      layout = Layout(width = '400px'),continuous_update = True,
                      description = 'Injected current delay [$ms$]:', style = style)

        predur= FloatSlider(value = 3000, min = 0, max = 3000,
                        description='Ascending triangular current duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posdur= FloatSlider(value = 11250, min = 0, max = 12000,
                        description='Descending triangular current duration [$ms$]:', 
                        layout = Layout(width= '400px'), style = style)

        posamp= FloatSlider(value = 12, min = -100, max = 50,
                        description='Ascending triangular current amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)
        possamp= FloatSlider(value = 27, min = -100, max = 50,
                        description='Descending triangular current amplitude [$nA$]:', 
                        layout = Layout(width= '400px'), style = style)

        ld= FloatSlider(value = 6150, min = 1000, max = 25000,
                        description='Dendrite lenght [$mm$]:', 
                        layout = Layout(width= '400px'), style = style)

        diam= FloatSlider(value = 50, min = 10, max = 300,
                        description='Dendrite diameter [$um$]:', 
                        layout = Layout(width= '400px'), style = style)
        return [mutype,gama,delay,predur,posdur, posamp, possamp,ld,diam,gnap,gcal,gks]

        

def widget_params_pulse():

    style = {'description_width': 'initial'}
    gks= widgets.FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    gcal= widgets.FloatSlider(value = 0.00001, min = 0.00001, max = 0.00062,
                    description='Calcium type-L conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    gnap= widgets.FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Motor Neuron Type:', style = style)

    gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Monoamnergic Drive:', style = style)

    delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                    description='Depolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                    description='Time between current pulses [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                    description='Hyperpolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    preamp= widgets.FloatSlider(value = 10, min = -30, max = 50,
                    description='Depolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= widgets.FloatSlider(value = -10, min = -30, max = 50,
                    description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= widgets.FloatSlider(value = 6150, min = 1000, max = 25000,
                    description='Dendrite Lenght[$mm$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam = widgets.FloatSlider(value = 50, min = 10, max = 300,
                    description='Dendrite Diameter[$um$]:', 
                    layout = Layout(width= '400px'), style = style)
    #parameters = widgets.HBox([widgets.VBox([mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks])])
    parameters = widgets.VBox([mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks])
    wp = {'mutype':mutype,'gama': gama, 'delay':delay,'predur': predur,'meddur': meddur,'posdur': posdur,'preamp': preamp,'posamp':posamp,'ld':ld,'diam':diam, 'gnap':gnap, 'gcal':gcal, 'gks':gks}
    #for i in parameters.children[0].children:
    for i in parameters.children:
        i.layout = widgets.Layout(width= '390px')
        i.style = style
        i.continuous_update = False
    return parameters,wp
    #return [mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks]
    
def widget_params_interact_manual_pulse():

    style = {'description_width': 'initial'}
    gks= widgets.FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    gcal= widgets.FloatSlider(value = 0.00001, min = 0.00001, max = 0.00062,
                    description='Calcium type-L conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    gnap= widgets.FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '500px'), style = style)

    mutype = widgets.Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Motor Neuron Type:', style = style)

    gama = widgets.Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Monoamnergic Drive:', style = style)

    delay = widgets.Dropdown(options = range(0,300,10), value = 290,
                  layout = Layout(width = '200px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= widgets.FloatSlider(value = 1500, min = 0, max = 5000,
                    description='Depolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    meddur= widgets.FloatSlider(value = 3000, min = 0, max = 5000,
                    description='Time between current pulses [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= widgets.FloatSlider(value = 1000, min = 0, max = 5000,
                    description='Hyperpolarizing current pulse duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    preamp= widgets.FloatSlider(value = 10, min = -30, max = 50,
                    description='Depolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= widgets.FloatSlider(value = -10, min = -30, max = 50,
                    description='Hyperpolarizing current pulse amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= widgets.FloatSlider(value = 6150, min = 1000, max = 25000,
                    description='Dendrite Lenght[$mm$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam = widgets.FloatSlider(value = 50, min = 10, max = 300,
                    description='Dendrite Diameter[$um$]:', 
                    layout = Layout(width= '400px'), style = style)
    return [mutype,gama,delay,predur,meddur,posdur,preamp,posamp,ld,diam,gnap,gcal,gks]


def widget_params_triangular():    
    style = {'description_width': 'initial'}
    gks= FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '450px'), style = style)

    gcal= FloatSlider(value = 0.00001, min = 0.00001, max = 0.000062,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gnap= FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = Dropdown(options = range(0,300,10), value = 20,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= FloatSlider(value = 3000, min = 0, max = 3000,
                    description='Ascending triangular current duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= FloatSlider(value = 11250, min = 0, max = 12000,
                    description='Descending triangular current duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= FloatSlider(value = 12, min = -100, max = 50,
                    description='Ascending triangular current amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)
    possamp= FloatSlider(value = 27, min = -100, max = 50,
                    description='Descending triangular current amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= FloatSlider(value = 6150, min = 1000, max = 25000,
                    description='Dendrite lenght [$mm$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam= FloatSlider(value = 50, min = 10, max = 300,
                    description='Dendrite diameter [$um$]:', 
                    layout = Layout(width= '400px'), style = style)
    
    parameters = widgets.VBox([mutype,gama,delay,predur,posdur,posamp,possamp,ld,diam,gnap,gcal,gks])
    wp = {'mutype':mutype,'gama': gama, 'delay':delay,'predur': predur,'posdur': posdur,'posamp': posamp,'possamp':possamp,'ld':ld,'diam':diam, 'gnap':gnap, 'gcal':gcal, 'gks':gks}
    #for i in parameters.children[0].children:
    for i in parameters.children:
        i.layout = widgets.Layout(width= '390px')
        i.style = style
        i.continuous_update = False
    return parameters,wp

def widget_interact_manual_triangular():    
    style = {'description_width': 'initial'}
    gks= FloatSlider(value = 0.018, min = 0.012, max = 0.030,
                    description='Slow potassium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '450px'), style = style)

    gcal= FloatSlider(value = 0.00001, min = 0.000001, max = 0.000062,
                    description='L-type calcium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    gnap= FloatSlider(value = 0.00052, min = 0.0001, max = 0.009,
                    description='Persistent sodium conductance [$mS/cm^2$]:', 
                    layout = Layout(width= '400px'), style = style)

    mutype = Dropdown(options = ['S', 'FR', 'FF'], value = 'S',
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Motor neuron type:', style = style)

    gama = Dropdown(options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], value = 1.,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Monoaminergic drive:', style = style)

    delay = Dropdown(options = range(0,300,10), value = 20,
                  layout = Layout(width = '400px'),continuous_update = True,
                  description = 'Injected current delay [$ms$]:', style = style)

    predur= FloatSlider(value = 3000, min = 0, max = 3000,
                    description='Ascending triangular current duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posdur= FloatSlider(value = 11250, min = 0, max = 12000,
                    description='Descending triangular current duration [$ms$]:', 
                    layout = Layout(width= '400px'), style = style)

    posamp= FloatSlider(value = 12, min = -100, max = 50,
                    description='Ascending triangular current amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)
    possamp= FloatSlider(value = 27, min = -100, max = 50,
                    description='Descending triangular current amplitude [$nA$]:', 
                    layout = Layout(width= '400px'), style = style)

    ld= FloatSlider(value = 6150, min = 1000, max = 25000,
                    description='Dendrite lenght [$mm$]:', 
                    layout = Layout(width= '400px'), style = style)

    diam= FloatSlider(value = 50, min = 10, max = 300,
                    description='Dendrite diameter [$um$]:', 
                    layout = Layout(width= '400px'), style = style)
    return [mutype,gama,delay,predur,posdur, posamp, possamp,ld,diam,gnap,gcal,gks]