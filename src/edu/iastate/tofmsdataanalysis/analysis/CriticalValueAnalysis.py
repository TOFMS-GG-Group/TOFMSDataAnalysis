import csv
import numpy as np
import random
import threading


class CriticalValueAnalysis:
    # Generates a random Poisson distribution of size s and lambda l and returns the distribution as a list.
    @staticmethod
    def generate_poisson_dist(l, s):
        return np.random.poisson(l, s)

    # Reads and processes the raw Ion Signal Histogram file with the name filename and returns a list of the data.
    @staticmethod
    def read_raw_ion_signal_histogram(filename):
        # TODO Add some magic here to process the file to make sure it works i.e remove junk data and make it a csv.
        reader = csv.reader(open(filename, "r"), delimiter=",")
        data = list(reader)

        del data[0]

        result = np.array(data).astype("float")
        smoothed_data = []

        for i in data:
            for j in range(int(i[1])):
                if float(i[0]) >= float(0.0):
                    smoothed_data.append(float(i[0]))

        return smoothed_data

    @staticmethod
    def generate_mean_value_from_ion_signal_histogram(ion_data):
        length = len(ion_data)
        sum = 0

        for i in range(length):
            sum += ion_data[i]

        return sum / length

    # Preforms a monte carlo simulation using the ion_data and poisson_data n times.
    # TODO Figure out how to multithread this to improve performance.
    # TODO Figure out how to include a timer so that I can time this method.
    @staticmethod
    def monte_carlo_simulation(ion_data, poisson_data, n):
        monte_carlo_data_results = []
        monte_carlo_sum_results = []

        for i in range(n):
            poisson_choice = random.choice(poisson_data)
            iteration_data = []
            sum = 0

            # TODO Should I round here or not?
            # TODO Convert this method into a sample method.
            if poisson_choice == 0:
                iteration_data.append(0)

                sum = 0

            for j in range(poisson_choice):
                data = random.choice(ion_data)
                iteration_data.append(data)

                sum += data

            monte_carlo_data_results.append(iteration_data)
            monte_carlo_sum_results.append(sum)


        return monte_carlo_sum_results
