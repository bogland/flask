from itertools import *
from operator import itemgetter
from collections import defaultdict,Counter

a = cycle([1,2,3]) # 1 2 3 1 2 3 1 2 3 ...
list_cycle = [a for a in zip([1,3,1],a)]
list_cycle.sort(key=lambda x:x[0]) # [(1,x),(1,x),(3,x)]
dict_groupby = {key: sorted(map(itemgetter(1), value)) for key, value 
in groupby(list_cycle, key=itemgetter(0))}
print(dict_groupby) # {1: [1, 3], 3: [2]} ,        value : (1, 1), (1, 3) 로 나옴 주의

counts = defaultdict(list)
attempts = [('dan', 87), ('erik', 95), ('jason', 79), ('erik', 97), ('dan', 100)]
for (name, score) in attempts:
    counts[name].append(score)
print(counts)

a = repeat(10, 3)  # 10 10 10 ...
a = chain('ABC', 'DEF') # [A B C D E F]
a = chain([1,2],[3,4]) # [1 2 3 4] 
a = compress('ABCDEF', [1,0,1,0,1,1]) # A C E F
a = zip_longest('AB', 'x', fillvalue='-') # [('A', 'x') ('B', '-')]
a = [k for k, g in groupby('AAAABBBCCDAABBB')] # A B C D A B
a = Counter('AAAABBB') # Counter({'A': 4, 'B': 3})
b = Counter('AB') # Counter({'A': 1, 'B': 1})
print(a - b, a & b) # - : Counter({'A': 3, 'B': 2}) & : min , | : max
a = product('ABCD', repeat=2) # [('A', 'A'), ('A', 'B'), ('A', 'C') ... , permutations, combinations
