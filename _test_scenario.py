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

def get_memory_usage(pid):
	command = run_command('ps -p ' + str(pid) + '-o %mem | head -2 | tail -1')
	result = command.communicate()[0].decode('utf-8').rstrip() 
	return result

def get_activemq_pid():
	result = run_command_back("sh ./helper_scripts/activemq_pid.sh")
	result.wait()
	result = pid.communicate()[0].decode('utf-8').rstrip()
	return result

def run(activemq_script):
	# Define variables to be used later on
	timestamp = get_timestamp()

	# Start Active MQ
	print("Starting Active MQ")
	run_command("sh ./helper_scripts/" + activemq_script)

	print("Waiting 8 seconds...")
	time.sleep(8)

	print("Starting tests");

	runner_receiver = run_command_back("python2 ./testing_scenario/read.py")
	runner_sender = run_command_back("python2 ./testing_scenario/run.py")
	runner_sender.wait()

	# Get the results
	results_file = open("./testing_scenario/account.txt", "r")
	result = results_file.read()
	results_file.close()

	print("Finished tests")

	# Kill dead active MQ
	print("Killing Active MQ...")
	activemq_process_kill = run_command('sh ./apache-activemq-5.13.2/bin/activemq stop')

	print("Waiting 3 seconds...")
	time.sleep(3)

	return result
