import json


class config:
    alpha_values = None
    num_ions = None
    elements_isotope_mapping = None
    elements_isotope_mapping = None
    sis_file_location = None
    signal_file_location = None
    output_file_location = None

    def __init__(self, path):
        with open(path) as f:
            config_file = json.load(f)

        self.alpha_values: list = config_file['alpha_values']
        self.num_ions: int = config_file['num_ions']

        self.elements_isotope_mapping: dict = config_file['isotope_element_mapping']

        self.sis_file_location: str = config_file['sis_file_location']
        self.signal_file_location: str = config_file['signal_file_location']
        self.output_file_location: str = config_file['output_file_location']
