import sys
import subprocess
import shlex

def run_command(cmd):
	cmd_args = shlex.split(cmd)
	print(cmd_args)
	subprocess.call(cmd_args)

for x in range(0,5):
<<<<<<< HEAD
	# run_command("python test_basic_with.py");
	run_command("python test_basic_without.py");
=======
	run_command("python test_basic_with.py");
	run_command("python test_basic_without.py");
>>>>>>> 58d2cfa1c3cc7f01728d7d929fd6be499bbd4f3a
