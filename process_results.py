import xlsxwriter
import time
import datetime
import os

RESULTS_DIRECTORY = 'results'
RUN_SIZES = [100, 200, 500, 1000, 5000, 10000, 20000, 100000]

def get_timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	return st

def get_results(filename):
	results_dictionary = {}
	file = open(RESULTS_DIRECTORY + '/' + filename)
	# Skip the first line
	file.readline()
	for line in file:
		line = line.replace('\n', '')
		split_result = line.split(',')
		results_dictionary[split_result[1]] = split_result[2]
	return results_dictionary

def write_row(worksheet, row_number, row_data):
	column_number = 0
	for item in row_data:
		worksheet.write(row_number, column_number, item)
		column_number += 1

def process_worksheet(workbook, result_type):
	worksheet = workbook.add_worksheet(result_type)
	header = ['Run'] + RUN_SIZES
	results = [header]

	# Iterate through all the result files on disk
	run_count = 0
	for fn in os.listdir(RESULTS_DIRECTORY):
		if fn.startswith(result_type):
			current_results_dictionary = get_results(fn);
			current_results = []
			for size in RUN_SIZES:
				current_result = current_results_dictionary.get(str(size), 'NIL')
				# If it's a number, convert it to a number, but otherwise leave it
				try:
					current_result = float(current_result)
				except ValueError:
					pass

				current_results.append(current_result)
			current_results.insert(0, run_count)
			results.append(current_results)
			run_count += 1

	row_number = 0
	for row_data in results:
		write_row(worksheet, row_number, row_data)
		row_number += 1

workbook_file_name = 'results_' + get_timestamp() + '.xlsx'
workbook = xlsxwriter.Workbook(RESULTS_DIRECTORY + '/' + workbook_file_name);

# Generate the 'with' results
process_worksheet(workbook, 'basic_with_')
process_worksheet(workbook, 'basic_without_')

workbook.close()
