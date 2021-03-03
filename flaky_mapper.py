from random import random
import sys

if random() < 0.5:
	raise SystemExit("I am Lucky")

for line in sys.stdin:
	pass

#local 모드에서는 시스템 중단
#분산 모드에서는 일부 에러가 출력되고 3개 중 1개는 성공.. 효과가 있음

from functools import reduce
import operator

reduce (operator.add, [1,4,9,16])
reduce (operator.add, [5,9,16])
reduce (operator.add, [14,16])

#map->reduce
reduce(operator.add, map(lambda x: x*x, [1,2,3,4]))
