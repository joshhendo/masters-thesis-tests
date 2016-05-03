# TEST WITH LOCk PROVIDER

printf "status,iterations,time\n" > results.txt

exec ./run_activemq.sh &
ACTIVEMQPID=$!

sleep 15s

exec python ./testing/send.py 10000 &
RESULT=python ./testing/read.py 10000 
printf "lock,10000,%s\n" "$RESULT" >> results.txt

kill $ACTIVEMQPID

sleep 2s

# TEST WITHOUT LOCK PROVIDER

exec ./run_activemq_without.sh &
ACTIVEMQPID=$!

sleep 7s

exec python ./testing/send.py 10000 &
RESULT=python ./testing/read.py 10000
printf "nolock,10000,%s\n" "$RESULT" >> results.txt


kill $ACTIVEMQPID


