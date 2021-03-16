from __future__ import print_function
from collections import Counter
import sys

for line in sys.stdin:
	article_id, content = line.split("\t", 1)
	words = content.split()
	counts = Counter(words)
	for word, word_count in counts.items():
		print(word, word_count, sep="\t")