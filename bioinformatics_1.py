# find pattern
s = 'ACTGTACGATGATGTGTGTCAAAG'
p = 'TGT'
cnt = 0
idx = 0
while True:
    idx = s.find(p, idx)
    if idx >= 0:
        cnt += 1
        idx += 1
    else:
        break
print(cnt)

# most common 3-mer
s='CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
length=len(s)-3+1
l=list()
for i in range(length):
    l.append(s[i:i+3])
c = {x:l.count(x) for x in l}

from collections import Counter

c = Counter(l)
c.most_common(1)