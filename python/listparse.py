# -*- coding: UTF-8 -*- 
# @author hezhang
# @date   2016/9/5 
# @time   17:54:20
# @brief  listparse paractice

iterItem = ('A', 'B', 'C')
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
miter    = [x for x in iterItem ]
# listparse  = map + filter
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers) )
# listparse
doubled_odds = [
        x * 2 
        for x in numbers 
        if x % 2 == 1
        ]
# for way
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)

# 集合解析式
words  = ['Here', 'I', 'am']
cfirst = set();
for w in words:
    cfirst.add(w[0])
# setparse
cfirst = {w[0] for w in words}
print(cfirst)

