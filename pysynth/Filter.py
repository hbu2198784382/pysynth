import scipy.signal

def lpf(data,samplerate,freqmin):
    """LowPass Filter - Pass the low frequencies,cut off the high frequencies.

    Args:
        data (ndarray): the data of the wave
        samplerate (int): the samplerate of the wave
        freqmin (int): the minimum of frequencies

    Returns:
        np.ndarray: the filtered data
    """
    wn = 2 * freqmin / samplerate
    b, a = scipy.signal.butter(8,wn,'lowpass')
    return scipy.signal.filtfilt(b,a,data)

def hpf(data,samplerate,freqmax):
    """HighPass Filter - Pass the high frequencies,cut off the low frequencies.

    Args:
        data (ndarray): the data of the wave
        samplerate (int): the samplerate of the wave
        freqmax (int): the maximum of frequencies

    Returns:
        np.ndarray: the filtered data
    """
    wn = 2 * freqmax / samplerate
    b, a = scipy.signal.butter(8,wn,'highpass')
    return scipy.signal.filtfilt(b,a,data)

def bpf(data,samplerate,freqmin,freqmax):
    """BandPass Filter - Pass the frequencies between the minimum and maximum

    Args:
        data (ndarray): the data of the wave
        samplerate (int): the samplerate of the wave
        freqmin (int): the minimum of the frequency
        freqmax (int): the maximum of the frequency

    Returns:
        np.ndarray: the filtered data
    """
    wn1 = 2 * freqmin / samplerate
    wn2 = 2 * freqmax / samplerate
    b, a = scipy.signal.butter(8,[wn1,wn2],'bandpass')
    return scipy.signal.filtfilt(b,a,data)

def bpf(data,samplerate,freqmin,freqmax):
    """BandStop Filter - Cut off the frequencies between the minimum and maximum

    Args:
        data (ndarray): the data of the wave
        samplerate (int): the samplerate of the wave
        freqmin (int): the minimum of the frequency
        freqmax (int): the maximum of the frequency

    Returns:
        np.ndarray: the filtered data
    """
    wn1 = 2 * freqmin / samplerate
    wn2 = 2 * freqmax / samplerate
    b, a = scipy.signal.butter(8,[wn1,wn2],'bandstop')
    return scipy.signal.filtfilt(b,a,data)