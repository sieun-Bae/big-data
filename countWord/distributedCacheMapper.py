from __future__ import print_function
import re
import sys

def read_vocabulary(file_path):
	return set(word.strip() for word in open(file_path))

male_names = read_vocabulary("names.tar/male.txt")
female_names = read_vocabulary("names.tar/femail.txt")

for line in sys.stdin:
	article_id, content = line.split("\t", 1)
	words = re.split("\W+", content)
	for word in words:
		if word in male_names or word in female_names:
			print(word, 1, sep="\t")
