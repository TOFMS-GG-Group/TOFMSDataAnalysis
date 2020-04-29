import h5py
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn


class hdf5processor():
    def process_signal_data(filename, element_isotope_map):
        hf = h5py.File(filename, 'r')

        n1 = np.array(hf["PeakData"]["PeakData"])
        raw_peak_data = np.array(hf["PeakData"]["PeakData"])

        reshaped_peak_data = np.reshape(raw_peak_data, (100000, 286))

        number_of_waveforms = int(hf.attrs['NbrWaveforms'])

        reshaped_peak_data_in_counts = reshaped_peak_data * number_of_waveforms

        isotopes = np.array(hf['PeakData']['PeakTable']['label'])
        isotopes_new = [None] * isotopes.size

        for i in range(isotopes.size):
            isotopes_new[i] = str(isotopes[i]).replace('b', '').replace('[', '').replace(']', '').replace('+',
                                                                                                          '').replace(
                '\'',
                '')
        n2 = np.reshape(n1, (100000, 286))
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

        return element_summed_data_map

    def plot_elements(self, data):
        for key, value in data.items():
            plt.plot(data.get(key), label=key)

        plt.legend()
        plt.show()

    def save_dataset(self, filename, elements_list, element_data):
        hf = h5py.File(filename, 'a')

        elements_list_ascii = [n.encode("ascii", "ignore") for n in list(elements_list.keys())]

        elements_list_dataset = hf.create_dataset("spWork/ElementList", (len(elements_list_ascii), 1), data=elements_list_ascii, dtype=h5py.string_dtype())

        # TODO Maybe find a way to convert this to ASCII or change them all the UTF8.
        iostopes_used = np.array([[b'Element', b'Isotope(s)', b'Null', b'Null', b'Null'], [b'Ti', b'47Ti', b'49Ti', b'Null', b'Null']], dtype='|S10')

        dt = h5py.special_dtype(vlen=str)

        hf.create_dataset("spWork/IsotopesUsed", iostopes_used.shape, data=iostopes_used, dtype=dt)

        hf.close()
