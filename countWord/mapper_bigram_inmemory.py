from __future__import print_function
from collections import Counter
import sys

current_word = None
bigram_count = Counter()

for line in sys.stdin:
	first_word, second_word, counts = line.split("\t", 2)
	counts = Counter({second_word: int(counts)})
	if first_word == current_word:
		bigram_count += counts
	else:
		if current_word:
			for second_word, bigram_count in bigram_count.items():
				print(current_word, second_word, 1)
	## memory 소요가 큼

'''
==> config에서 설정

yarn --config $HADOOP_EMPTY_CONFIG jar $HADOOP_STREAMING_JAR \
	-D stream.num.map.output.key.fields = 2 \
	-files bigram_mapper.py, bigram_reducer.py \
	-mapper 'pyton bigram_mapper.py' \
	-reducer 'python bigram_reducer.py' \
	-numReduceTasks 5 \
	-input wikipedia_sample.txt \
	-output word_count
'''