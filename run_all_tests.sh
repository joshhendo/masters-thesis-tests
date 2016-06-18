#!/bin/bash

for i in {1..5}
do
	python test_basic_with.py
	python test_basic_without.py
done

python process_results.py