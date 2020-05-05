# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:13:19 2017

@author: debora
"""

from itertools import chain

def choose_mu_type(soma,dend):
    mutype = raw_input('S, FR or FF: ')
    if mutype == "S":
        print ('slow twitch')
        mus(soma,dend)
    elif mutype == "FR":
        print ('fast twitch, fatigue resistant')
        mufr(soma,dend)
    elif mutype == "FF":
        print ('fast twitch, fatigable')
        muff(soma,dend)

def mus(soma,dend):
    # soma parameters
    soma.L = 80
    soma.nseg = 1
    soma.diam = 80
    soma.Ra = 70.0 #resistividade citoplasmatica
    soma.cm = 1.0

    soma.gnabar_napp =  0.05
    soma.gnapbar_napp = .00052
    soma.gkfbar_napp = 0.0028
    soma.gksbar_napp = 0.018
    soma.mact_napp = 13.0
    soma.rinact_napp = 0.025
    soma.ena = 120.0
    soma.ek = -10.0
    soma.el_napp = 0.0
    soma.vtraub_napp = 0.0
    soma.gl_napp = 1/1100.0

    # dendrite parameters
    dend.L = 6150.0
    dend.nseg = 1
    dend.diam = 50
    dend.Ra = 70.0
    dend.cm = 1.0
    
    dend.gcaLbar_caL = 0.000010#0.00001056
    dend.ecaL = 140
    dend.vtraub_caL = 36.25#35
    dend.gama_caL = 1.
    dend.Ltau_caL = 80
    dend.gl_caL = 1/12550.0
    dend.el_caL = 0.0


def mufr(soma,dend):
        # soma parameters
        soma.L = 85
        soma.nseg = 1
        soma.diam = 85
        soma.Ra = 70.0
        soma.cm = 1.0

        soma.gnabar_napp = 0.07
        soma.gnapbar_napp = 0.0008
        soma.gkfbar_napp = 0.0040
        soma.gksbar_napp = 0.037
        soma.mact_napp= 17.0
        soma.rinact_napp = 0.058
        soma.ena = 120.0
        soma.ek = -10.0
        soma.el_napp = 0.0
        soma.vtraub_napp = 0.0
        soma.gl_napp = 1/1000.0

        # dendrite parameters
        dend.L = 7450.0
        dend.nseg = 1
        dend.diam = 73
        dend.Ra = 70.0
        dend.cm = 1.0
        
        dend.gcaLbar_caL = 0.000007
        dend.ecaL = 140
        dend.vtraub_caL = 35.6
        dend.gama_caL = 1
        dend.Ltau_caL = 46
        dend.gl_caL = 1/8825.0
        dend.el_caL = 0.0


def muff(soma,dend):
    # soma parameters
    soma.L = 100.25
    soma.nseg = 1
    soma.diam = 100.25
    soma.Ra = 70.0
    soma.cm = 1.0

    soma.gnabar_napp = 0.075 
    soma.gnapbar_napp = .00065 ##
    soma.gkfbar_napp = 0.00135
    soma.gksbar_napp = 0.016 ###
    soma.mact_napp = 19.2
    soma.rinact_napp = 0.062
    soma.ena = 120.0
    soma.ek = -10.0
    soma.el_napp = 0.0
    soma.vtraub_napp = 0.0
    soma.gl_napp = 1/800.0

    # dendrite parameters
    dend.L = 9350 ##
    dend.nseg = 1
    dend.diam = 88#88 ##
    dend.Ra = 70.0
    dend.cm = 1.0
    
    dend.gcaLbar_caL = 0.0000062
    dend.ecaL = 140
    dend.vtraub_caL = 34
    dend.gama_caL = 0.2
    dend.Ltau_caL = 47
    dend.gl_caL = 1/6500.0
    dend.el_caL = 0.0


