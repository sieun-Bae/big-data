from __future__ import print_function
import sys

current_word = None #현재 key tracking
word_count = 0

for line in sys.stdin:
	word, counts = line.split("\t", 1)
	counts = int(counts)
	if word == current_word:
		word_count += counts
	else:
		if current_word:
			print(current_word, word_count, sep="\t")
		current_word = word
		word_count = counts

if current_word:
	print(current_word, word_count, sep="\t")