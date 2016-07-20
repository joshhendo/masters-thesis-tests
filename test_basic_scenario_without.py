import _test_scenario

activemq_script = "run_activemq_without.sh"

results_file = open('results_scenario_without.txt', 'w')

for i in range(0, 2):
	result = _test_scenario.run(activemq_script)
	results_file.write(result)
	results_file.write('\n')

results_file.close()

