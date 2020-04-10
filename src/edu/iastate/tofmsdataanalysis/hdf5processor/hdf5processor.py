import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt


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
        isotopes_new[i] = str(isotopes[i]).replace('b', '').replace('[', '').replace(']', '').replace('+', '').replace(
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


def plot_elements(data):
    for key, value in data.items():
        plt.plot(data.get(key), label=key)

    plt.legend()
    plt.show()


def save_dataset(filename, elements_list, element_data):
    hf = h5py.File(filename, 'a')

    asciiList = [n.encode("ascii", "ignore") for n in list(elements_list.keys())]
    hf.create_dataset("spWork/ElementList", (len(asciiList), 1), 'S10', asciiList)

    labels = [['Element', 'Isotope(s)']]

    hf.create_dataset("spWork/IsotopesUsed", (len(asciiList), 1), 'S10', asciiList)

    hf.close()


def main(argv):
    elements = {
        'Ti': ['47Ti', '49Ti'],
        'Cr': ['52Cr', '53Cr'],
        'Fe': ['54Fe', '57Fe'],
        'Mn': ['55Mn']}

    element_data = process_signal_data(
        argv[0],
        elements)

    plot_elements(element_data)

    save_dataset(argv[1], elements, element_data)


if __name__ == "__main__":
    main(sys.argv[1:])
