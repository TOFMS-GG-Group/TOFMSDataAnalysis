# TOFSDataAnalysis Project

WHAT IS THIS?
-------------

This application is for preforming data analysis on time of flight mass spectrometery. 

HOW TO USE THIS
---------------
1. Create your ```SIS.csv``` by making a csv file from the your ```SIS.txt``` file (Make sure to remove any not data like column titles).
2. Create a ```config.json``` and structure it like the ```config-sample.json```. Make sure to fill out each parameter correctly with correct paths.
3. Run `pip install -r requirements.txt` to install dependencies
6. Run `python app.py "PATH_TO_THE_CONFIG_JSON"` e.g. (Windows) ```python app.py "C:\\Users\Tyler Jaacks\\Desktop\\config.json"``` (Mac) ```python app.py "/Users/tylerjaacks/Desktop/config.json```
7. Open the h5 file in h5 viewer and enjoy.


DEVELOPMENT
-----------

If you want to work on this application we’d love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem or feature request fully.
2. Please thoroughly test your feature of bug fix.

CREDITS
-------

Tyler Jaacks <tjaacks@iastate> or <tylerjaacks@gmail.com>

Alexander Gundlach-Graham <alexgg@iastate.edu>