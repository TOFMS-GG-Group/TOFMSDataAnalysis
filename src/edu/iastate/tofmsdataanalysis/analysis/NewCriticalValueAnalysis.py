import csv
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.0001
numIons = 1000

SquareRootOfCountsArray = np.linspace(0.5, 5.0, num=50)
CountRateArray = SquareRootOfCountsArray**2

# TODO Add some magic here to process the file to make sure it works i.e remove junk data and make it a csv.
reader = csv.reader(open("D:\\tjaacks\TOFMSDataAnalysis\\test_data\\ISUSummedData.csv", "r"), delimiter=",")
data = list(reader)

SingleIonData = []

for i in data:
    for j in range(int(i[1])):
        if float(i[0]) >= float(0.0):
            SingleIonData.append(float(i[0]))

SingleIonSignal = np.mean(SingleIonData)

SISArrayNormalized = np.true_divide(SingleIonData, SingleIonSignal)

NetCriticalValueArray = np.array([])

for i in CountRateArray:
    Counts = np.random.poisson(i, numIons)
    CompoundArray = np.array([])

    for j in Counts:
        Draws = np.random.choice(SISArrayNormalized, j)
        Compound = sum(Draws)
        CompoundArray = np.append(CompoundArray, Compound)
        AverageCompound = np.mean(CompoundArray)

    Quantile = np.quantile(CompoundArray, (1 - alpha))
    NetCriticalValue = Quantile - AverageCompound
    NetCriticalValueArray = np.append(NetCriticalValueArray, NetCriticalValue)

X = SquareRootOfCountsArray
Y = NetCriticalValueArray

Coefficient = np.polyfit(X, Y, 1)
Poly1DFunction = np.poly1d(Coefficient)

plt.plot(X, Y, 'yo', X, Poly1DFunction(X), '--k')

plt.xlim(0, 5)
plt.ylim(0, 50)

plt.show()