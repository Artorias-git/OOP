import math
from itertools import *

def is_simple(val):
    count = 2  #cразу учтём 1 и val
    i = 2
    while i < math.sqrt(val):
        if val % i == 0:
            count += 2
        i += 1
    if (val % math.sqrt(val) == 0):
        count += 1
    return count == 2

simpls = []

for i in range(1, 1000000):
    if is_simple(i):
        simpls.append(i)
        print(i)

numbers = []
i = 0
for i in simpls:
    print(i)
    s = list(permutations(str(i)))
    num = []

    for j in range(len(s)):
        a = ""
        for k in range(len(s[j])):
            a = a + s[j][k]
        num.append(int(a))

    token = 0
    for g in range(len(num)):
        if is_simple(num[g]):
            continue
        else:
            token = 1
    if token == 1:
        token = 0
        continue
    else:
        numbers.append(i)

print(numbers)





