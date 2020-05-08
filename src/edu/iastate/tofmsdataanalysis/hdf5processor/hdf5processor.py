import h5py
import os.path
from os import path
import numpy as np
import matplotlib.pyplot as plt


class hdf5processor:
    @staticmethod
    def process_signal_data(input_filename, element_isotope_map):
        hf = h5py.File(input_filename, 'r')

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

    @staticmethod
    def plot_elements(data):
        for key, value in data.items():
            plt.plot(data.get(key), label=key)

        plt.legend()
        plt.show()

    @staticmethod
    def save_dataset(output_filename, alpha, critical_values, element_data, elements_isotope_mapping):
        dt = h5py.special_dtype(vlen=str)

        if path.exists(output_filename):
            os.remove(output_filename)

        hf = h5py.File(output_filename, 'a')

        elements_list_ascii = [n.encode("ascii", "ignore") for n in list(elements_isotope_mapping.keys())]

        hf.create_dataset("spWork/ElementList", (len(elements_list_ascii), 1), data=elements_list_ascii, dtype=h5py.string_dtype())

        isotopes_used = np.empty([len(elements_isotope_mapping) + 1, 4], dtype=dt)

        isotopes_used.fill(b'Null')

        isotopes_used[0, :] = [b'Element', b'Isotope(s)', b'Null', b'Null']

        i = 1

        # TODO Maybe find a way to convert this to ASCII or change them all the UTF8.
        for key in elements_isotope_mapping.keys():
            value = elements_isotope_mapping.get(key)

            iso1 = b'Null'
            iso2 = b'Null'
            iso3 = b'Null'

            print(key)
            print(value)

            if len(value) == 1:
                iso1 = value[0]
            elif len(value) == 2:
                iso1 = value[0]
                iso2 = value[1]
            elif len(value) == 3:
                iso1 = value[0]
                iso2 = value[1]
                iso3 = value[2]

            isotopes_used[i, :] = [key, iso1, iso2, iso3]

            i += 1

        hf.create_dataset("spWork/IsotopesUsed", isotopes_used.shape, data=isotopes_used, dtype=dt)

        critical_value_data = np.empty([len(critical_values) + 1, 3], dtype=dt)

        critical_value_data.fill(b'Null')

        critical_value_data[0, :] = [b'alpha', b'slope', b'intercept']

        for i in range(1, len(critical_value_data)):
            alpha_value = alpha[i - 1]
            slope_value = critical_values[i - 1][0]
            intercept_value = critical_values[i - 1][1]

            critical_value_data[i, :] = [alpha_value, slope_value, intercept_value]

        hf.create_dataset("spWork/CriticalValueExp", critical_value_data.shape, data=critical_value_data, dtype=dt)

        hf.close()
