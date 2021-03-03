from __future__ import print_function
import re
import sys

#reporter_mapper
for line in sys.stdin:
	article_id, content = line.split("\t", 1)
	words = re.findall("\w+", content)
	for index, word in enumerate(words):
		print(word, 1, sep="\t")
		print("reporter:status:processed {} words".format(index+1), file=sys.stderr)
	print("reporter:counter:Personal Counters, word found, 1", file=sys.stderr)
	#######################<group>, <counter>, <amount>
