#!/bin/bash

# TEST WITHOUT LOCK PROVIDER

echo "status,iterations,time\n" > results_without.txt

sh ./run_activemq_without.sh
sleep 15s

# Declare arrays of iterations
declare -a arr=("100" "200" "500" "1000" "5000" "10000" "20000" "100000")
for i in "${arr[@]}"
do
   exec python ./testing/send.py $i &
	RESULT="$(python ./testing/read.py $i)"
	echo "lock,$i,$RESULT" >> results.txt
done

./apache-activemq-5.13.2/bin/activemq stop
