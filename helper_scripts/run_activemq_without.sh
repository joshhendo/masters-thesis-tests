#!/bin/bash

cd ..

# Exit script if it encounters an error (e.g. during compilation)
set -e

# Check that apache-activemq-5.13.2 exists
if [ ! -d "apache-activemq-5.13.2" ]; then
	curl "http://apache.mirror.serversaustralia.com.au/activemq/5.13.2/apache-activemq-5.13.2-bin.tar.gz" -o apache-activemq-5.13.2-bin.tar.gz
	tar -zxvf apache-activemq-5.13.2.tar.gz
	rm apache-activemq-5.13.2.tar.gz
fi 

# Run Active MQ
./apache-activemq-5.13.2/bin/activemq start
