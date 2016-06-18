Works best on Linux.

Ensure Java is installed
```
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
```

Ensure Maven is installed
```
$ sudo apt install maven
```

Unfortunately, the library used for sending messages only works in Python 2, so it's important to have python2 aliased. The runner script is written in Python 3 (and will make a popen call to start the send and read scripts in Python 2 as appropriate).

To install the stomp library in python2, run:
```
python2   -m pip install stompy
```

To run the scripts, ensure you run it from the base directory and go
```
python test_basic_with.py
```

This will start Active MQ, start the tests, write the results to the results directory, and kill Active MQ.

For processing of results, you will need `xlsxwriter`. This can be installed with
```
python -m pip install xlsxwriter
```
