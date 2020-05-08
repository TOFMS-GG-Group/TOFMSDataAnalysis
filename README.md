# TOFSDataAnalysis Project

WHAT IS THIS?
-------------

This application is for preforming data analysis on time of flight mass spectrometery.

FILES NEEDED FOR THIS PROCESS
-----------------------------

1. ```SIS.txt``` this is the single ion signal from your Inductively Coupled Plasma Time-of-Flight Mass Spectrometer (ICP-TOFMS). At this time you will need to convert this to a csv file and remove any additional non data text such as column titles.
2. ```Data.h5``` this file may be named differntly but this the file containing all the data from your Spectrometer.
3. ```config.json``` this should contain things like the paths to your files above as well as an output path for the final h5 file, alpha values, number of ions, and you element to isotope mappings. A sample one can be found in the test_data folder.

HOW TO USE THIS
---------------

1. Follow the instruction above creating the files need to start the operation.
2. Run `pip install -r requirements.txt` to install dependencies
3. Run `python app.py "PATH_TO_THE_CONFIG_JSON"` e.g. (Windows) ```python app.py "C:\\Users\Tyler Jaacks\\Desktop\\config.json"``` (Mac) ```python app.py "/Users/tylerjaacks/Desktop/config.json```
4. Open the h5 file in h5 viewer and enjoy.


DEVELOPMENT
-----------

If you want to work on this application we’d love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem or feature request fully.
2. Please thoroughly test your feature of bug fix.

CREDITS
-------

Tyler Jaacks <tjaacks@iastate> or <tylerjaacks@gmail.com>

Alexander Gundlach-Graham <alexgg@iastate.edu>
