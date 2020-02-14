import edu.iastate.tofsdataanalysis.analysis.CriticalValueAnalysis as cva

poisson_data = cva.CriticalValueAnalysis.generate_poisson_dist(0.1, 100000)
ion_data = cva.CriticalValueAnalysis.read_raw_ion_signal_histogram("D:\\tjaacks\\SumHistogramSeries.csv")
mean_value = cva.CriticalValueAnalysis.generate_mean_value_from_ion_signal_histogram(ion_data)
monte_carlo_results = cva.CriticalValueAnalysis.monte_carlo_simulation(ion_data, poisson_data, 100000)

print("Poisson Data: " + str(poisson_data))
print("Ion Data: " + str(ion_data))
print("Mean Value: " + str(mean_value))
print("Monte Carlo Results: " + str(monte_carlo_results))
print("Length of Data : " + str(len(monte_carlo_results)))

print("Length of Range: " + str(range(len(monte_carlo_results))))

result_csv = open("D:\\data.csv", "w")
text = ""

for i in range(len(monte_carlo_results)):
    text += (str(i) + "," + str(monte_carlo_results[i] / mean_value) + "\n")

result_csv.write(text)
result_csv.close()
