import sys

from edu.iastate.tofmsdataanalysis.analysis import critical_value_analysis
from edu.iastate.tofmsdataanalysis.hdf5processor.hdf5processor import hdf5processor


def main(argv):
    # arg0: alpha, arg1: numIons, arg2: sisLocation
    # critical_value_analysis.CriticalValueAnalysis.calculate_critical_value(argv[0], argv[1], argv[2])

    elements = {
        'Ti': ['47Ti', '49Ti'],
        'Cr': ['52Cr', '53Cr'],
        'Fe': ['54Fe', '57Fe'],
        'Mn': ['55Mn']}

    # arg3: signalData
    element_data = hdf5processor.process_signal_data(argv[3], elements)

    #hdf5processor.plot_elements(element_data)

    # arg4: outputFile
    hdf5processor.save_dataset(argv[4], elements, element_data)


if __name__ == "__main__":
    main(sys.argv[1:])