from stompy.simple import Client
import sys

import time
import threading
import random
import os

time.sleep(0.5)

queue_name = "/queue/test4"

stomp = Client()
stomp.connect()

def get_random_time():
	rand = random.random()
	rand = rand * 500
	rand = rand / 1000
	return rand

def send_message(body, retries=20):
	try:
		stomp.put(body, destination=queue_name, persistent=False)
	except:
		print("Exception caught")
		if (retries > 0):
			time.sleep(0.05)
			send_message(body, retries-1)
		else:
			print("Ran out of retries")


def send_withdraw():
	time.sleep(get_random_time())
	send_message("{\"message\": \"transaction\", \"type\": \"withdraw\", \"userid\": \"12345678\", \"amount\": 20.00}")

def send_deposit():
	time.sleep(get_random_time())
	send_message("{\"message\": \"transaction\", \"type\": \"deposit\", \"userid\": \"12345678\", \"amount\": 50.00}")

# Deleting the account.txt file
if os.path.exists('account.txt'):
	os.remove('account.txt')

# Seed the account with $100
f = open('account.txt', 'w')
f.write('100.00')
f.close()

time.sleep(1)

# start the threads to send the message in a random order
threading.Thread(target=send_withdraw).start()
threading.Thread(target=send_deposit).start()

time.sleep(3)

stomp.disconnect()
