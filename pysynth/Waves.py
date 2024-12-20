import numpy as np


class Wave():
    def __init__(self,samplerate,time):
        self.sr = samplerate
        self.time = time
        self.data = np.ndarray([])
    
    def __call__(self):
        return self.data
    
    def append(self,data:np.ndarray):
        self.data = np.concatenate(self.data,data)
    
    def sleep(self,stime):
        self.append(np.zeros(self.sr*stime))
        

def sinwave(freq,stime,samplerate):
    tn = np.linspace(0,stime,samplerate*stime,endpoint=False)
    return np.sin(2*np.pi*freq*tn)
