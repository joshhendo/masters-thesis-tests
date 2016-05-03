from stompy.simple import Client
import time
from timeit import default_timer as timer
import sys

queue_name = "/queue/test4"

if (len(sys.argv) < 2):
	print("Usage: read.py expected_count")
	exit()

# How many messages are we expecting to come in?
expected = int(sys.argv[1])

count = 0

start = None
end = None

stomp = Client()
stomp.connect()

stomp.subscribe(queue_name, "client")

while (count < expected):
	try: 
		frame = stomp.get()
		if start is None:
			start = timer()
		count = count + 1
		stomp.ack(frame)
	except:
		print("got nothing :(")
		time.sleep(1)

end = timer()

result = (end - start)

print(str(result))

stomp.unsubscribe(queue_name)
stomp.disconnect()
