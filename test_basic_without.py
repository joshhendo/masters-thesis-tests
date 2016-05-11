import _test_basic

iterations = { 100, 200, 500, 1000, 5000, 10000, 20000, 100000 }
results_name = "basic_without"
activemq_script = "run_activemq_without.sh"

_test_basic.run(iterations, results_name, activemq_script)