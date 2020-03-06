import string

import h5py
import numpy as np
import matplotlib.pyplot as plt

hf = h5py.File('D:\\Test.h5', 'r')

raw_peak_data = np.array(hf["PeakData"]["PeakData"])

reshaped_peak_data = np.reshape(raw_peak_data, (100000, 286))

number_of_waveforms = int(hf.attrs['NbrWaveforms'])

reshaped_peak_data_in_counts = reshaped_peak_data * number_of_waveforms

isotopes = np.array(hf['PeakData']['PeakTable']['label'])
isotopes_new = [None] * isotopes.size

for i in range(isotopes.size):
    isotopes_new[i] = str(isotopes[i]).replace('b', '').replace('[', '').replace(']', '').replace('+', '').replace('\'',
                                                                                                                   '')

element_isotope_map = {
    'Ti': ['47Ti', '49Ti'],
    'Cr': ['52Cr', '53Cr'],
    'Fe': ['54Fe', '57Fe'],
    'Mn': ['55Mn']}

element_summed_data_map = {}

for key, value in element_isotope_map.items():
    if len(value) == 1:
        element_summed_data_map.update({key: reshaped_peak_data_in_counts[:, isotopes_new.index(value[0])]})
    elif len(value) == 2:
        new_summed_data = reshaped_peak_data_in_counts[:, isotopes_new.index(value[0])] + \
                          reshaped_peak_data_in_counts[:, isotopes_new.index(value[1])]

        element_summed_data_map.update({key: new_summed_data})
    elif len(value) == 3:
        new_summed_data = reshaped_peak_data_in_counts[:, isotopes_new.index(value[0])] + \
                          reshaped_peak_data_in_counts[:, isotopes_new.index(value[1])] + \
                          reshaped_peak_data_in_counts[:, isotopes_new.index(value[2])]

        element_summed_data_map.update({key: new_summed_data})

plt.plot(element_summed_data_map.get('Ti'), label="Ti")
plt.plot(element_summed_data_map.get('Cr'), label="Cr")
plt.plot(element_summed_data_map.get('Fe'), label="Fe")
plt.legend()
plt.show()
