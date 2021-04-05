import nolds
import os
import mne
import json
import numpy as np

# -- epileptologie-bonn.de --
def txt_lyapunov(txt):
    archivo = open(txt,'r')
    Serie=[ int(dat[:dat.find('\n')]) for dat in archivo]
    lyapunov = nolds.lyap_r(Serie)
    return lyapunov
def txt_hurst(txt):
    archivo = open(txt,'r')
    Serie=[ int(dat[:dat.find('\n')]) for dat in archivo]
    hurst = nolds.hurst_rs(Serie)
    return hurst
def txt_corr_dim(txt,dim):
    archivo = open(txt,'r')
    Serie=[ int(dat[:dat.find('\n')]) for dat in archivo]
    corr = nolds.corr_dim(Serie, dim)
    return corr
def txt_entropy(txt, dim):
    archivo = open(txt,'r')
    Serie=[ int(dat[:dat.find('\n')]) for dat in archivo]
    samp = nolds.sampen(Serie, dim)
    return samp
#--- BRAIN VISION ----
def vhdr_lyapunov(vhdr,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(vhdr)
            raw = mne.io.read_raw_brainvision(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.lyap_r(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(vhdr,time)
            print('.......')

        EEG={}
        EEG['paciente'] = vhdr[vhdr.find('RES'):vhdr.find('RES')+8]
        EEG['sensor']   = channel_index
        EEG['situacion']= vhdr[vhdr.find('SIT'):vhdr.find('SIT')+12]
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def vhdr_hurst(vhdr,tmax,inter,electrodes):

    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(vhdr)
            raw = mne.io.read_raw_brainvision(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.hurst_rs(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(vhdr,time)
            print('.......')

        EEG={}
        EEG['paciente'] = vhdr[vhdr.find('RES'):vhdr.find('RES')+8]
        EEG['sensor']   = channel_index
        EEG['situacion']= vhdr[vhdr.find('SIT'):vhdr.find('SIT')+12]
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def vhdr_corr_dim(vhdr,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(vhdr)
            raw = mne.io.read_raw_brainvision(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.corr_dim(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(vhdr,time)
            print('.......')

        EEG={}
        EEG['paciente'] = vhdr[vhdr.find('RES'):vhdr.find('RES')+8]
        EEG['sensor']   = channel_index
        EEG['situacion']= vhdr[vhdr.find('SIT'):vhdr.find('SIT')+12]
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def vhdr_entropy(vhdr,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(vhdr)
            raw = mne.io.read_raw_brainvision(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.sampen(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(vhdr,time)
            print('.......')

        EEG={}
        EEG['paciente'] = vhdr[vhdr.find('RES'):vhdr.find('RES')+8]
        EEG['sensor']   = channel_index
        EEG['situacion']= vhdr[vhdr.find('SIT'):vhdr.find('SIT')+12]
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
# --- EDF ---
def edf_lyapunov(edf,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(edf)
            raw = mne.io.read_raw_edf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.lyap_r(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def edf_hurst(edf,tmax,inter,electrodes):

    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(edf)
            raw = mne.io.read_raw_edf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.hurst_rs(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def edf_corr_dim(edf,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(edf)
            raw = mne.io.read_raw_edf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.corr_dim(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def edf_entropy(edf,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(edf)
            raw = mne.io.read_raw_edf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.sampen(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
# --- BDF ---
def bdf_lyapunov(bdf,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(bdf)
            raw = mne.io.read_raw_bdf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.lyap_r(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def bdf_hurst(bdf,tmax,inter,electrodes):

    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(bdf)
            raw = mne.io.read_raw_bdf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.hurst_rs(Serie)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def bdf_corr_dim(bdf,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(bdf)
            raw = mne.io.read_raw_bdf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.corr_dim(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
def bdf_entropy(bdf,dim,tmax,inter,electrodes):
    div=tmax/inter
    sep_time=[]
    for i in range(inter):
        sep_time.append([div*i,div*(i+1)])

    data=[]

    for electrode in electrodes:
        vec_cof=[]
        for time in sep_time:

            sample_data_raw_file = os.path.join(bdf)
            raw = mne.io.read_raw_bdf(sample_data_raw_file)

            sampling_freq = raw.info['sfreq']
            start_stop_seconds = np.array(time)
            start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
            channel_index = electrode
            raw_selection = raw[channel_index, start_sample:stop_sample]

            Serie=[i for i in raw_selection[0][0]]
            coef_LP=nolds.sampen(Serie, dim)# Lyapunov exponent (Rosenstein et al.)
            vec_cof.append(coef_LP)
            print('.......')
            print(time)
            print('.......')

        EEG={}
        EEG['sensor']   = channel_index
        EEG['media']    = np.mean(vec_cof)
        EEG['varianza'] = np.var(vec_cof)

        data.append(EEG)
    return data
