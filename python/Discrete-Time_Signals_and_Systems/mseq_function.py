
# coding: utf-8

#### Import libraries
import numpy as np


#### Function Definition 
def get_tap(baseVal, powerVal):
    """
    get tap array of current baseVal and powerVal 
    
        INPUT:
        baseVal  -number of sequence levels (2,3, or 5 allowed)
        powerVal -power, so that sequence length is baseVal^powerVal-1
    """
    tap = []
    if baseVal == 2:
        if powerVal == 2:
            tap = [[1, 2]]
            
        elif powerVal == 3:
            tap = [[1, 3], [2, 3]]
            
        elif powerVal == 4: 
            tap[0] = [[1, 4], [3, 4]]
            
        elif powerVal == 5: 
            tap = [[2, 5],
                   [3, 5],
                   [1, 2, 3, 5],
                   [2, 3, 4, 5],
                   [1, 2, 4, 5],
                   [1, 3, 4, 5]]
            
        elif powerVal == 6: 
            tap = [[1, 6],
                   [5, 6],
                   [1, 2, 5, 6],
                   [1, 4, 5, 6],
                   [1, 3, 4, 6],
                   [2, 3, 5, 6]]
            
        elif powerVal == 7: 
            tap = [[1, 7],
                   [6, 7],
                   [3, 7],
                   [4, 7],
                   [1, 2, 3, 7],
                   [4, 5, 6, 7],
                   [1, 2, 5, 7],
                   [2, 5, 6, 7],
                   [2, 3, 4, 7],
                   [3, 4, 5, 7],
                   [1, 3, 5, 7],
                   [2, 4, 6, 7],
                   [1, 3, 6, 7],
                   [1, 4, 6, 7],
                   [2, 3, 4, 5, 6, 7],
                   [1, 2, 3, 4, 5, 7],
                   [1, 2, 4, 5, 6, 7],
                   [1, 2, 3, 5, 6, 7]]
        
        elif powerVal == 8: 
            tap = [[1, 2, 7, 8],
                   [1, 6, 7, 8],
                   [1, 3, 5, 8],
                   [3, 5, 7, 8],
                   [2, 3, 4, 8],
                   [4, 5, 6, 8],
                   [2, 3, 5, 8],
                   [3, 5, 6, 8],
                   [2, 3, 6, 8],
                   [2, 5, 6, 8],
                   [2, 3, 7, 8],
                   [1, 5, 6, 8],
                   [1, 2, 3, 4, 6, 8],
                   [2, 4, 5, 6, 7, 8],
                   [1, 2, 3, 6, 7, 8],
                   [1, 2, 5, 6, 7, 8]]
            
        elif powerVal == 9: 
            tap = [[4, 9],
                   [5, 9],
                   [3, 4, 6, 9],
                   [3, 5, 6, 9],
                   [4, 5, 8, 9],
                   [1, 4, 5, 9],
                   [1, 4, 8, 9],
                   [1, 5, 8, 9],
                   [2, 3, 5, 9],
                   [4, 6, 7, 9],
                   [5, 6, 8, 9],
                   [1, 3, 4, 9],
                   [2, 7, 8, 9],
                   [1, 2, 7, 9],
                   [2, 4, 7, 9],
                   [2, 5, 7, 9],
                   [2, 4, 8, 9],
                   [1, 5, 7, 9],
                   [1, 2, 4, 5, 6, 9],
                   [3, 4, 5, 7, 8, 9],
                   [1, 3, 4, 6, 7, 9],
                   [2, 3, 5, 6, 8, 9],
                   [3, 5, 6, 7, 8, 9],
                   [1, 2, 3, 4, 6, 9],
                   [1, 5, 6, 7, 8, 9],
                   [1, 2, 3, 4, 8, 9],
                   [1, 2, 3, 7, 8, 9],
                   [1, 2, 6, 7, 8, 9],
                   [1, 3, 5, 6, 8, 9],
                   [1, 3, 4, 6, 8, 9],
                   [1, 2, 3, 5, 6, 9],
                   [3, 4, 6, 7, 8, 9],
                   [2, 3, 6, 7, 8, 9],
                   [1, 2, 3, 6, 7, 9],
                   [1, 4, 5, 6, 8, 9],
                   [1, 3, 4, 5, 8, 9],
                   [1, 3, 6, 7, 8, 9],
                   [1, 2, 3, 6, 8, 9],
                   [2, 3, 4, 5, 6, 9],
                   [3, 4, 5, 6, 7, 9],
                   [2, 4, 6, 7, 8, 9],
                   [1, 2, 3, 5, 7, 9],
                   [2, 3, 4, 5, 7, 9],
                   [2, 4, 5, 6, 7, 9],
                   [1, 2, 4, 5, 7, 9],
                   [2, 4, 5, 6, 7, 9],
                   [1, 3, 4, 5, 6, 7, 8, 9],
                   [1, 2, 3, 4, 5, 6, 8, 9]]
        
        elif powerVal == 10: 
            tap = [[3, 10],
                   [7, 10],
                   [2, 3, 8, 10],
                   [2, 7, 8, 10],
                   [1, 3, 4, 10],
                   [6, 7, 9, 10],
                   [1, 5, 8, 10],
                   [2, 5, 9, 10],
                   [4, 5, 8, 10],
                   [2, 5, 6, 10],
                   [1, 4, 9, 10],
                   [1, 6, 9, 10],
                   [3, 4, 8, 10],
                   [2, 6, 7, 10],
                   [2, 3, 5, 10],
                   [5, 7, 8, 10],
                   [1, 2, 5, 10],
                   [5, 8, 9, 10],
                   [2, 4, 9, 10],
                   [1, 6, 8, 10],
                   [3, 7, 9, 10],
                   [1, 3, 7, 10],
                   [1, 2, 3, 5, 6, 10],
                   [4, 5, 7, 8, 9, 10],
                   [2, 3, 6, 8, 9, 10],
                   [1, 2, 4, 7, 8, 10],
                   [1, 5, 6, 8, 9, 10],
                   [1, 2, 4, 5, 9, 10],
                   [2, 5, 6, 7, 8, 10],
                   [2, 3, 4, 5, 8, 10],
                   [2, 4, 6, 8, 9, 10],
                   [1, 2, 4, 6, 8, 10],
                   [1, 2, 3, 7, 8, 10],
                   [2, 3, 7, 8, 9, 10],
                   [3, 4, 5, 8, 9, 10],
                   [1, 2, 5, 6, 7, 10],
                   [1, 4, 6, 7, 9, 10],
                   [1, 3, 4, 6, 9, 10],
                   [1, 2, 6, 8, 9, 10],
                   [1, 2, 4, 8, 9, 10],
                   [1, 4, 7, 8, 9, 10],
                   [1, 2, 3, 6, 9, 10],
                   [1, 2, 6, 7, 8, 10],
                   [2, 3, 4, 8, 9, 10],
                   [1, 2, 4, 6, 7, 10],
                   [3, 4, 6, 8, 9, 10],
                   [2, 4, 5, 7, 9, 10],
                   [1, 3, 5, 6, 8, 10],
                   [3, 4, 5, 6, 9, 10],
                   [1, 4, 5, 6, 7, 10],
                   [1, 3, 4, 5, 6, 7, 8, 10],
                   [2, 3, 4, 5, 6, 7, 9, 10],
                   [3, 4, 5, 6, 7, 8, 9, 10],
                   [1, 2, 3, 4, 5, 6, 7, 10],
                   [1, 2, 3, 4, 5, 6, 9, 10],
                   [1, 4, 5, 6, 7, 8, 9, 10],
                   [2, 3, 4, 5, 6, 8, 9, 10],
                   [1, 2, 4, 5, 6, 7, 8, 10],
                   [1, 2, 3, 4, 6, 7, 9, 10],
                   [1, 3, 4, 6, 7, 8, 9, 10]]
            
        elif powerVal == 11:
            tap = [[9, 11]]
            
        elif powerVal == 12:
            tap = [[6, 8, 11, 12]]
            
        elif powerVal == 13:
            tap = [[9, 10, 12, 13]]
            
        elif powerVal == 14:
            tap = [[4, 8, 13, 14]]
            
        elif powerVal == 15: 
            tap =[[14, 15]]
            
        elif powerVal == 16: 
            tap = [[4, 13, 15, 16]] 
            
        elif powerVal == 17:
            tap = [[14, 17]]
            
        elif powerVal == 18:
            tap = [[11, 18]]
            
        elif powerVal == 19:
            tap = [[14, 17, 18, 19]]
            
        elif powerVal == 20:
            tap = [[17, 20]]
            
        elif powerVal == 21:
            tap = [[19, 21]]
            
        elif powerVal == 22:
            tap = [[21, 22]]
            
        elif powerVal == 23:
            tap = [[18, 23]]
            
        elif powerVal == 24:
            tap = [[17, 22, 23, 24]]
            
        elif powerVal == 25:
            tap = [[22, 25]]
            
        elif powerVal == 26:
            tap = [[20, 24, 25, 26]]
            
        elif powerVal == 27:
            tap = [[22, 25, 26, 27]]
            
        elif powerVal == 28:
            tap = [[25, 28]]
            
        elif powerVal == 29:
            tap = [[27, 29]]
            
        elif powerVal == 30:
            tap = [[7, 28, 29, 30]]

        else:
            raise Exception('M-sequence %f^%f is not defined'%(baseVal,powerVal))

    if baseVal == 3:
        
        if powerVal == 2:
            tap  = [[2, 1], [1, 1]]
            
        elif powerVal == 3:
            tap = [[0, 1, 2],
                   [1, 0, 2],
                   [1, 2, 2],
                   [2, 1, 2]]
        
        elif powerVal == 4:
            tap = [[0, 0, 2, 1],
                   [0, 0, 1, 1],
                   [2, 0, 0, 1],
                   [2, 2, 1, 1],
                   [2, 1, 1, 1],
                   [1, 0, 0, 1],
                   [1, 2, 2, 1],
                   [1, 1, 2, 1]]
        
        elif powerVal == 5:
            tap = [[0, 0, 0, 1, 2],
                   [0, 0, 0, 1, 2],
                   [0, 0, 1, 2, 2],
                   [0, 2, 1, 0, 2],
                   [0, 2, 1, 1, 2],
                   [0, 1, 2, 0, 2],
                   [0, 1, 1, 2, 2],
                   [2, 0, 0, 1, 2],
                   [2, 0, 2, 0, 2],
                   [2, 0, 2, 2, 2],
                   [2, 2, 0, 2, 2],
                   [2, 2, 2, 1, 2],
                   [2, 2, 1, 2, 2],
                   [2, 1, 2, 2, 2],
                   [2, 1, 1, 0, 2],
                   [1, 0, 0, 0, 2],
                   [1, 0, 0, 2, 2],
                   [1, 0, 1, 1, 2],
                   [1, 2, 2, 2, 2],
                   [1, 1, 0, 1, 2],
                   [1, 1, 2, 0, 2]]
        
        elif powerVal == 6:
            tap = [[0, 0, 0, 0, 2, 1],
                   [0, 0, 0, 0, 1, 1],
                   [0, 0, 2, 0, 2, 1],
                   [0, 0, 1, 0, 1, 1],
                   [0, 2, 0, 1, 2, 1],
                   [0, 2, 0, 1, 1, 1],
                   [0, 2, 2, 0, 1, 1],
                   [0, 2, 2, 2, 1, 1],
                   [2, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 1],
                   [1, 0, 2, 1, 0, 1],
                   [1, 0, 1, 0, 0, 1],
                   [1, 0, 1, 2, 1, 1],
                   [1, 0, 1, 1, 1, 1],
                   [1, 2, 0, 2, 2, 1],
                   [1, 2, 0, 1, 0, 1],
                   [1, 2, 2, 1, 2, 1],
                   [1, 2, 1, 0, 1, 1],
                   [1, 2, 1, 2, 1, 1],
                   [1, 2, 1, 1, 2, 1],
                   [1, 1, 2, 1, 0, 1],
                   [1, 1, 1, 0, 1, 1],
                   [1, 1, 1, 2, 0, 1],
                   [1, 1, 1, 1, 1, 1]]
        
        elif powerVal == 7:
            tap = [[0, 0, 0, 0, 2, 1, 2],
                   [0, 0, 0, 0, 1, 0, 2],
                   [0, 0, 0, 2, 0, 2, 2],
                   [0, 0, 0, 2, 2, 2, 2],
                   [0, 0, 0, 2, 1, 0, 2],
                   [0, 0, 0, 1, 1, 2, 2],
                   [0, 0, 0, 1, 1, 1, 2],
                   [0, 0, 2, 2, 2, 0, 2],
                   [0, 0, 2, 2, 1, 2, 2],
                   [0, 0, 2, 1, 0, 0, 2],
                   [0, 0, 2, 1, 2, 2, 2],
                   [0, 0, 1, 0, 2, 1, 2],
                   [0, 0, 1, 0, 1, 1, 2],
                   [0, 0, 1, 1, 0, 1, 2],
                   [0, 0, 1, 1, 2, 0, 2],
                   [0, 2, 0, 0, 0, 2, 2],
                   [0, 2, 0, 0, 1, 0, 2],
                   [0, 2, 0, 0, 1, 1, 2],
                   [0, 2, 0, 2, 2, 0, 2],
                   [0, 2, 0, 2, 1, 2, 2],
                   [0, 2, 0, 1, 1, 0, 2],
                   [0, 2, 2, 0, 2, 0, 2],
                   [0, 2, 2, 0, 1, 2, 2],
                   [0, 2, 2, 2, 2, 1, 2],
                   [0, 2, 2, 2, 1, 0, 2],
                   [0, 2, 2, 1, 0, 1, 2],
                   [0, 2, 2, 1, 2, 2, 2]]
        else:
            raise Exception('M-sequence %f^%f is not defined'%(baseVal,powerVal))

    if baseVal == 5: 
        
        if powerVal == 2:
            tap = [[4, 3],
                   [3, 2],
                   [2, 2],
                   [1, 3]]
            
        elif powerVal == 3:
            tap = [[0, 2, 3],
                   [4, 1, 2],
                   [3, 0, 2],
                   [3, 4, 2],
                   [3, 3, 3],
                   [3, 3, 2],
                   [3, 1, 3],
                   [2, 0, 3],
                   [2, 4, 3],
                   [2, 3, 3],
                   [2, 3, 2],
                   [2, 1, 2],
                   [1, 0, 2],
                   [1, 4, 3],
                   [1, 1, 3]]
        
        elif powerVal == 4:
            tap = [[0, 4, 3, 3],
                   [0, 4, 3, 2],
                   [0, 4, 2, 3],
                   [0, 4, 2, 2],
                   [0, 1, 4, 3],
                   [0, 1, 4, 2],
                   [0, 1, 1, 3],
                   [0, 1, 1, 2],
                   [4, 0, 4, 2],
                   [4, 0, 3, 2],
                   [4, 0, 2, 3],
                   [4, 0, 1, 3],
                   [4, 4, 4, 2],
                   [4, 3, 0, 3],
                   [4, 3, 4, 3],
                   [4, 2, 0, 2],
                   [4, 2, 1, 3],
                   [4, 1, 1, 2],
                   [3, 0, 4, 2],
                   [3, 0, 3, 3],
                   [3, 0, 2, 2],
                   [3, 0, 1, 3],
                   [3, 4, 3, 2],
                   [3, 3, 0, 2],
                   [3, 3, 3, 3],
                   [3, 2, 0, 3],
                   [3, 2, 2, 3],
                   [3, 1, 2, 2],
                   [2, 0, 4, 3],
                   [2, 0, 3, 2],
                   [2, 0, 2, 3],
                   [2, 0, 1, 2],
                   [2, 4, 2, 2],
                   [2, 3, 0, 2],
                   [2, 3, 2, 3],
                   [2, 2, 0, 3],
                   [2, 2, 3, 3],
                   [2, 1, 3, 2],
                   [1, 0, 4, 3],
                   [1, 0, 3, 3],
                   [1, 0, 2, 2],
                   [1, 0, 1, 2],
                   [1, 4, 1, 2],
                   [1, 3, 0, 3],
                   [1, 3, 1, 3],
                   [1, 2, 0, 2],
                   [1, 2, 4, 3],
                   [1, 1, 4, 2]]
            
        else:
            raise Exception('M-sequence %f^%f is not defined'%(baseVal,powerVal))

    return tap


def mseq(baseVal, powerVal, shift = 1, whichSeq = 1):
    """
    Maximum length sequence assuming 2,3,5 distinct values

        [ms]=MSEQ(baseVal,powerVal[,shift,whichSeq])

        OUTPUT:
        ms = generated maximum length sequence, of length basisVal^powerVal-1

        INPUT:
        baseVal  -number of sequence levels (2,3, or 5 allowed)
        powerVal -power, so that sequence length is baseVal^powerVal-1
        shift    -cyclical shift of the sequence
        whichSeq -sequence istantiation to use 
        (numer of sequences varies with powreVal - see the code)

    Example: ms=mseq(2,3,1,2) generates a binary sequence of length $2^3$-1
         shifted cyclically by 1 step and using the second set of weights

    original matlab code (C) Written by Giedrius T. Buracas, SNL-B, Salk Institute 
    Register values are taken from: WDT Davies, System Identification
    for self-adaptive control. Wiley-Interscience, 1970
    When using mseq code for design of FMRI experiments, please, cite:
    G.T.Buracas & G.M.Boynton (2002) Efficient Design of Event-Related fMRI 
    Experiments Using M-sequences. NeuroImage, 16, 801-813.
    """

    bitNum = baseVal**powerVal - 1
    register = np.ones(powerVal)
    tap = get_tap(baseVal, powerVal)
    ms = np.zeros((bitNum, 1))

    if not whichSeq:
        whichSeq = np.ceil(np.random.rand(1)*len(tap)) 
    elif whichSeq > len(tap) | whichSeq < 1 :
            print(' wrapping arround!')
            whichSeq = np.remainder(whichSeq, len(tap)) + 1
    
    # weights
    weights = np.zeros( powerVal)
    
    if baseVal == 2:
        index = [x-1 for x in tap[int(whichSeq)-1]]
        for i in range(len(index)):
            weights[index[i]] = 1
    elif baseVal > 2:
        weights = tap[whichSeq-1]

    for i in range(0, bitNum): 
        # calculating next digit with modulo powerVal 
        # arithmetic register, (tap[0])
        # ms(i)= rem(sum(register(tap[whichSeq]),baseVal)
        ms[i] =  np.remainder(np.dot(weights, register)+baseVal, baseVal)
        # updating the register
        register = np.append(ms[i], register[0:powerVal-1])

    ms = ms[:]
    
    if shift:
        shift = np.remainder(shift, len(ms))
        ms = np.append(ms[shift:], ms[0:shift])

    if baseVal == 2:
        ms = ms*2 - 1
    elif baseVal == 3:
        for i in range(len(ms)):
            if ms[i] == 2:
                ms[i] = -1
    elif baseVal == 5:
        for i in range(len(ms)):
            if ms[i] == 4:
                ms[i] = -1
            if ms[i] == 3:
                ms[i] = -2
    else:
        raise Exception('wrong baseVal!')
        
    return ms

