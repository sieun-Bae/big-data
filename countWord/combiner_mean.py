from __future__ import print_function
import sys

current_word = None
word_count, article_count = 0,0

for line in sys.stdin:
	word, articles, counts = line, split("\t", 2)
	articles, counts = int(articles), int(counts)
	if word == current_word:
		word_count += counts
		article_count += articles
	else:
		if current_word:
			assert len(current_word.rstrip()) > 0
			print(current_word, word_count, article_count, sep="\t")
		current_word = word
		word_count = counts
		article_count = articles

if current_word:
	print(current_word, word_count, article_count, sep="\t")