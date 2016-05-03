from stompy.simple import Client
import sys

import time

time.sleep(2)

queue_name = "/queue/test4"

if (len(sys.argv) < 2):
	print("Usage: send.py total")
	exit()

total = int(sys.argv[1])
count = 0

stomp = Client()
stomp.connect()

while (count < total):
	stomp.put("{\"message\": \"addUser\", \"userid\": \"" + str(count) + "\"}", destination=queue_name, persistent=False)
	count = count + 1;

stomp.disconnect()
