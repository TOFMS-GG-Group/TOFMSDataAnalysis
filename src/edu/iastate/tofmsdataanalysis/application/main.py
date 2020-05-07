import sys

from edu.iastate.tofmsdataanalysis.analysis import critical_value_analysis
from edu.iastate.tofmsdataanalysis.hdf5processor.hdf5processor import hdf5processor


# arg0: alpha, arg1: numIons, arg2: sisLocation, arg3: signalData, arg4: outputLocation
def main(argv):
    elements_isotope_mapping = {
        'Ti': ['47Ti', '49Ti'],
        'Cr': ['52Cr', '53Cr'],
        'Fe': ['54Fe', '57Fe'],
        'Mn': ['55Mn']}

    critical_values = critical_value_analysis.CriticalValueAnalysis.calculate_critical_value(argv[0], argv[1], argv[2])

    element_data = hdf5processor.process_signal_data(argv[3], elements_isotope_mapping)

    hdf5processor.plot_elements(element_data)
    hdf5processor.save_dataset(sys.argv[4],
                               critical_values,
                               element_data,
                               elements_isotope_mapping)


if __name__ == "__main__":
    main(sys.argv[1:])
