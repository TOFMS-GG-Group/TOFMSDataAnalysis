import csv

import numpy as np


# Contains the code for preform the critical analysis.
class CriticalValueAnalysis:
    # Calculates a critical value from a alpha value, number of ion signals, and a file with the single ion signals.
    # This function returns an array with slope and intercept of the critical value.
    @staticmethod
    def calculate_critical_value(alpha, num_ions, filename):
        reader = csv.reader(open(filename, "r"), delimiter=",")
        data = list(reader)

        del data[0]

        result = np.array(data).astype("float")
        SIS_Array = []

        result = np.array(data).astype("float")
        SIS_Array = []

        for i in data:
            for j in range(int(i[1])):
                if float(i[0]) >= float(0.0):
                    SIS_Array.append(float(i[0]))

        SIS_Value = np.average(SIS_Array)

        SIS_Array_Norm = np.true_divide(SIS_Array, SIS_Value)

        # SqRtCrRateArray is the a linearly space (Lambda)^0.5 values used for creating the Poisson Dist.
        # CtRateArray is the array of lambda values for determining the cmpd Poisson distribution.
        SqRtCtRateArray = np.linspace(0.5, 5, num=50)
        CtRateArray = SqRtCtRateArray ** 2

        cts_array = np.random.poisson(lam=(CtRateArray), size=(int(num_ions), len(CtRateArray)))
        cmpd_array = cts_array.transpose()

        # below: all count rates from the array poisson-distributed count rates are indexed
        # and the sum of the a random draw for each Poisson count is taken from the SIS_Array_Norm
        # and then these random draws are summed together and stored in the cmpd_array, which
        # is the array of Cmpd_Poisson Values for all lambda values tested.

        count = 0

        with np.nditer(cmpd_array, flags=['multi_index'], op_flags=['readwrite']) as it:
            for x in it:
                print("Monte Carlo Simulation " + str(count + 1))
                x[...] = sum(np.random.choice(SIS_Array_Norm, x))
                count += 1

        l_c_array = np.array([])

        for i in range(0, len(CtRateArray)):
            OneLambdaArray = cmpd_array[i]
            avg_OneLambdaArray = np.mean(OneLambdaArray)
            s_c = np.quantile(OneLambdaArray, (1 - float(alpha)))
            l_c = s_c - avg_OneLambdaArray
            l_c_array = np.append(l_c_array, l_c)

        x = SqRtCtRateArray
        y = l_c_array

        return np.polyfit(x, y, 1)
