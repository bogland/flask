from itertools import *
from operator import itemgetter
from collections import defaultdict,Counter
import heapq
import re 

#Tuple List to GroupBy
a = cycle([1,2,3]) # 1 2 3 1 2 3 1 2 3 ...
list_cycle = [a for a in zip([1,3,1],a)]
list_cycle.sort(key=lambda x:x[0]) # [(1,x),(1,x),(3,x)]
dict_groupby = {key: sorted(map(itemgetter(1), value)) for key, value #map자체론 실행되지 않음에 주의
in groupby(list_cycle, key=itemgetter(0))}
dict_groupby # {1: [1, 3], 3: [2]} ,        value : (1, 1), (1, 3) 로 나옴 주의

#DefaultDict
counts = defaultdict(list)
attempts = [('dan', 87), ('erik', 95), ('jason', 79), ('erik', 97), ('dan', 100)]
for (name, score) in attempts:
    counts[name].append(score)
counts

#IterTools
a = repeat(10, 3)  # 10 10 10 ...
a = chain('ABC', 'DEF') # [A B C D E F]
a = chain([1,2],[3,4]) # [1 2 3 4] 
a = compress('ABCDEF', [1,0,1,0,1,1]) # A C E F
a = zip_longest('AB', 'x', fillvalue='-') # [('A', 'x') ('B', '-')]
a = [k for k, g in groupby('AAAABBBCCDAABBB')] # A B C D A B
a = Counter('AAAABBB') # Counter({'A': 4, 'B': 3})
b = Counter('AB') # Counter({'A': 1, 'B': 1})
(a - b, a & b) # - : Counter({'A': 3, 'B': 2}) & : min , | : max
a = product('ABCD', repeat=2) # [('A', 'A'), ('A', 'B'), ('A', 'C') ... , permutations, combinations

#Heapq
heap = [] # defaultdict(list)은 안되네
heapq.heappush(heap, (3,3))
heapq.heappush(heap, (1,1))
heapq.heappush(heap, (2,2))
min = heapq.heappop(heap) #제일작은 (1,1) pop

#Regex
words = re.findall(r'\bf[a-z]*', 'which foot or fell') #['foot', 'fell']
words = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10') #[('width','20'),('height','10')]
words = re.findall(r'\d','1,2,3,4')
words = re.findall(r'"(.*?)"','"hello"') # ['hello']
words = re.search(r'[\w]+','123,123') #없으면 None, span(),start(),end()

text = '.+.lemons and limes.-.'
word = text.strip('.+')  # 양끝에서 벗겨냄, lemons and limes.-
word = text.find("o")  # 6 
word = "-".join(["a", "b", "c"]) #a-b-c
state = "l" in text # True
