import h5py
import numpy as np

hf = h5py.File('D:\\Test.h5', 'r')

n1 = np.array(hf["PeakData"]["PeakData"])

n2 = np.reshape(n1, (100000, 286))

print(n2)