import sys

from edu.iastate.tofmsdataanalysis.analysis import critical_value_analysis
from edu.iastate.tofmsdataanalysis.application import config
from edu.iastate.tofmsdataanalysis.hdf5processor.hdf5processor import hdf5processor


def main(argv):
    print("Loading configuration file.")

    config_file = config.config(argv[0])

    print("Starting the critical analysis phase...")

    critical_values = [0, 0, 0, 0]

    for i in range(len(config_file.alpha_values)):
        critical_values[i] = critical_value_analysis \
            .CriticalValueAnalysis.calculate_critical_value(config_file.alpha_values[i],
                                                            config_file.num_ions,
                                                            config_file.sis_file_location)
    print("Starting the signal processing phase...")

    element_data = hdf5processor.process_signal_data(config_file.signal_file_location,
                                                     config_file.elements_isotope_mapping)

    print("Saving the data to an HDF5 file....")

    hdf5processor.save_dataset(config_file.output_file_location,
                               config_file.alpha_values,
                               critical_values,
                               element_data,
                               config_file.elements_isotope_mapping)

    print("Finished")


if __name__ == "__main__":
    main(sys.argv[1:])
