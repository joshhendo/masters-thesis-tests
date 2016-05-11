# This file should be imported and the following variables passed in
#iterations = { 100, 200, 500, 1000, 5000, 10000, 20000, 100000 }
#results_name = "basic_with"
#activemq_script = "run_activemq.sh"


import sys
import time
import datetime
import subprocess

def get_timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	return st

def run_command(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def run(iterations, results_name, activemq_script):
	# Define variables to be used later on
	timestamp = get_timestamp()

	# Start Active MQ
	print("Starting Active MQ")
	activemq_process = run_command("sh ./helper_scripts/" + activemq_script)

	print("Waiting 15 seconds...")
	time.sleep(15)

	print("Starting tests");
	filename = "./results/" + results_name + "_" + timestamp
	file = open(filename,"w")
	file.write("status,iterations,time\n")

	for i in iterations:
		print("Running: " + str(i))
		runner_receiver = run_command("python2 ./testing/read.py " + str(i))
		runner_sender = run_command("python2 ./testing/send.py " + str(i))
		runner_sender.wait()

		# Get the stdout from the runner, decode it and strip the newline
		result = runner_receiver.communicate()[0].decode('utf-8').rstrip()
		print("result for " + str(i) + " is " + str(result))
		file.write("lock," + str(i) + "," + str(result) + "\n")
		print(i)

	file.close()

	print("Finished tests")

	# Kill dead active MQ
	print("Killing Active MQ...")
	activemq_process.kill();
	activemq_process_kill = run_command('./apache-activemq-5.13.2/bin/activemq stop')
	activemq_process_kill.wait();
