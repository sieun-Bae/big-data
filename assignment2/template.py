import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

for line in sys.stdin:
	try:
		article_id, text = unicode(line.strip()).split('\t',1)
	except ValueError as e:
		continue
	text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
    	eprint("reporter:counter:Wiki stats,Total words, %d"%1)
    	print("%s\t%d"%(word.lower(), 1))