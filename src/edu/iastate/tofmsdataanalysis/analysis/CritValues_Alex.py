import csv
import sys

import matplotlib.pyplot as plt
import numpy as np


def critical_value_analysis(filename):
    # alpha is false positive percentage for determining the critical value
    alpha = 0.0001

    numIons = 100000

    reader = csv.reader(open(filename, "r"), delimiter=",")
    data = list(reader)

    del data[0]

    result = np.array(data).astype("float")
    SIS_Array = []

    for i in data:
        for j in range(int(i[1])):
            if float(i[0]) >= float(0.0):
                SIS_Array.append(float(i[0]))
    # print(SIS_Array)

    SIS_Value = np.average(SIS_Array)
    # print(SIS_Value)

    SIS_Array_Norm = np.true_divide(SIS_Array, SIS_Value)
    # print(SIS_Array_Norm)

    # SqRtCrRateArray is the a linearly space (Lambda)^0.5 values used for creating the Poisson Dist.
    # CtRateArray is the array of lambda values for determining the cmpd Poisson distribution.
    SqRtCtRateArray = np.linspace(0.5, 5, num=50)
    CtRateArray = SqRtCtRateArray ** 2

    cts_array = np.random.poisson(lam=(CtRateArray), size=(numIons, len(CtRateArray)))
    cmpd_array = cts_array.transpose()

    # below: all count rates from the array poisson-distributed count rates are indexed
    # and the sum of the a random draw for each Poisson count is taken from the SIS_Array_Norm
    # and then these random draws are summed together and stored in the cmpd_array, which
    # is the array of Cmpd_Poisson Values for all lambda values tested.

    with np.nditer(cmpd_array, flags=['multi_index'], op_flags=['readwrite']) as it:
        for x in it:
            x[...] = sum(np.random.choice(SIS_Array_Norm, x))

    l_c_array = np.array([])
    for i in range(0, len(CtRateArray)):
        OneLambdaArray = cmpd_array[i]
        avg_OneLambdaArray = np.mean(OneLambdaArray)
        s_c = np.quantile(OneLambdaArray, (1 - alpha))
        l_c = s_c - avg_OneLambdaArray
        l_c_array = np.append(l_c_array, l_c)

    x = SqRtCtRateArray
    y = l_c_array

    coef = np.polyfit(x, y, 1)
    poly1d_fn = np.poly1d(coef)
    print(coef)
    # poly1d_fn is now a function which takes in x and returns an estimate for y

    plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
    plt.xlim(0, 5)
    plt.ylim(0, 25)
    plt.show()


def main(argv):
    critical_value_analysis(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
