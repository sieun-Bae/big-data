from __future__ import print_function
import re
import sys
for line in sys.stdin:
	article_id, content = line.split("\t", 1)
	words = re.split("\W+", content)
	for index in range(len(words)-1):
		print(words[index], words[index+1], 1, sep="\t")
## memory 소요가 큼