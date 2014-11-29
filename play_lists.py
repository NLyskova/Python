#Chapter 8  Lists

import numpy as np

a=[1,2,3,4,5,6,7,8,9,10]
b=[9,8,7,6,5,4,3,2,1,0]
c=a+b
print c, len(c)
d1=np.add(a, b)
print d1, len(d1)
d2=[x + y for x, y in zip(a, b)]
print d2, len(d2)
d3=[a[i]+b[i] for i in range(len(a))]
print d3, len(d3)

print [x*y for x,y in zip(a,b)]
print np.multiply(a, b)

#Most list methods are void; they modify the list and return None.
t = ['d', 'c', 'e', 'b', 'a']
t1=t.sort()
print t
print t1



