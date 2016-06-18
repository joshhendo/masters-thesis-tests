# This file should be imported and the following variables passed in
#iterations = { 100, 200, 500, 1000, 5000, 10000, 20000, 100000 }
#results_name = "basic_with"
#activemq_script = "run_activemq.sh"


import sys
import time
import datetime
import subprocess
import shlex

def get_timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	return st

def run_command(cmd):
	cmd_args = shlex.split(cmd)
	print(cmd_args)
	subprocess.call(cmd_args)

def run_command_back(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def run(iterations, results_name, activemq_script):
	# Define variables to be used later on
	timestamp = get_timestamp()

	# Start Active MQ
	print("Starting Active MQ")
	run_command("sh ./helper_scripts/" + activemq_script)

	print("Waiting 8 seconds...")
	time.sleep(8)

	print("Starting tests");
	filename = "./results/" + results_name + "_" + timestamp
	file = open(filename,"w")
	file.write("status,iterations,time\n")

	for i in iterations:
		print("Running: " + str(i))
		print("Starting Read")
		runner_receiver = run_command_back("python2 ./testing/read.py " + str(i))
		print("Starting Send")
		runner_sender = run_command_back("python2 ./testing/send.py " + str(i))
		print("Waiting for Send to Finish")
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
	activemq_process_kill = run_command('sh ./apache-activemq-5.13.2/bin/activemq stop')

	print("Waiting 3 seconds...")
	time.sleep(3)
