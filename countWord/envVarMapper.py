from __future__ import print_function
import re
import sys

if os.environ["mapred_task_is_map"] == "true":
	print("input_file:{}, start:{}, size:{}".format(
		os.environ["mapreduce_map_input_file"],
		os.environ["mapreduce_map_input_start"],
		os.environ["mapreduce_map_input_length"],))

##or to start with given "input start index"
'''
if os.environ["mapred_task_is_map"] == "true":
	split_input_start = int(os.environ["mapreduce_map_input_start"])
for split_line_index, line in enumerate(sys.stdin):
	line_number = split_line_index + split_input_start
	if (line_number < 10):
		print(line_number, line, sep='\t')
'''

##or to start with given "word pattern"
'''
pattern = re.compile(os.environ["word_pattern"])
=> should give env var with -D option in shell script
	ex) yarn jar $HADOOP_STREAMING_JAR -D word_pattern = "\w+\d+"
'''
for line in sys.stdin:
	pass

