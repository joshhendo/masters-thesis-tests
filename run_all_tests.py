import sys
import subprocess
import shlex

def run_command(cmd):
	cmd_args = shlex.split(cmd)
	print(cmd_args)
	subprocess.call(cmd_args)

for x in range(0,5):
	# run_command("python test_basic_with.py");
	run_command("python test_basic_without.py");
