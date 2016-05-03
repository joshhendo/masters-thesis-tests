#!/bin/bash

# Exit script if it encounters an error (e.g. during compilation)
set -e

# Check that activemq-isolation-plugin exists, if not, clone it
if [ ! -d "activemq-isolation-plugin" ]; then
	git clone https://github.com/joshhendo/activemq-isolation-plugin.git
fi

# Compile
cd ./activemq-isolation-plugin 
/opt/apache-maven-3.3.9/bin/mvn clean install

cd ..

# Check that apache-activemq-5.13.2 exists
if [ ! -d "apache-activemq-5.13.2" ]; then
	curl "http://apache.mirror.serversaustralia.com.au/activemq/5.13.2/apache-activemq-5.13.2-bin.tar.gz" -o apache-activemq-5.13.2-bin.tar.gz
	tar -zxvf apache-activemq-5.13.2-bin.tar.gz
	rm apache-activemq-5.13.2.tar.gz
fi 

# Download libraries
cd ./apache-activemq-5.13.2/lib

if [ ! -f commons-lang3-3.4.jar ]; then
    curl "http://central.maven.org/maven2/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.jar" -o "commons-lang3-3.4.jar"
fi

if [ ! -f gson-2.6.2.jar ]; then
	curl "http://central.maven.org/maven2/com/google/code/gson/gson/2.6.2/gson-2.6.2.jar" -o "gson-2.6.2.jar"
fi

if [ ! -f json-20160212.jar ]; then
	curl "http://central.maven.org/maven2/org/json/json/20160212/json-20160212.jar" -o "json-20160212.jar"
fi

cd ./../..

cp ./activemq-isolation-plugin/target/activemq-isolation.jar ./apache-activemq-5.13.2/lib/

# Run Active MQ
./apache-activemq-5.13.2/bin/activemq start xbean:file:./activemq-isolation-plugin/src/main/resources/org/apache/activemq/isolation/activemq-isolation.xml
