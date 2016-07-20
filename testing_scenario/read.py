from stompy.simple import Client
import time
from timeit import default_timer as timer
import sys
import json
import threading

queue_name = "/queue/test4"


def process_frame(frame):
	j = json.loads(frame.body)
	t = j['type']
	alter_amount = float(j['amount'])
	print("Got message: " + t)

	# read the amount
	f = open('account.txt', 'r')
	amount = float(f.read())
	f.close()

	print("current amount is: " + str(amount))

	# takes 2 seconds!!?
	time.sleep(0.2)

	if (t == 'deposit'):
		amount += alter_amount
	if (t == 'withdraw'):
		amount -= alter_amount
	
	f = open('account.txt', 'w')
	f.write(str(amount))
	f.close()

	print("Ack message: " + j['message'])
	stomp.ack(frame)


stomp = Client()
stomp.connect()

stomp.subscribe(queue_name, "client")

while (True):
	try: 
		frame = stomp.get()
		threading.Thread(target=process_frame, args=(frame,)).start()
		# j = json.loads(frame.body)
		# print(j['message'])
		# stomp.ack(frame)
	except:
		print("got nothing :(")
		time.sleep(1)


stomp.unsubscribe(queue_name)
stomp.disconnect()
