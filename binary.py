import sys
import sys

n = int(input().strip())
b = int(bin(n)[2:])
count=0
counts = []
while b:
    rem = b%10
    if rem==1:
        count+=1
    else:
        counts.append(count)
        count=0
    b=b//10
counts.append(count)
print(max(counts))
        # quot = n//2
        # count = 0
        # count_new = 0
        # while quot>0:
        # rem = n%2
        # if rem == 1:
        # count = count + 1
        # if count_new < count:
        # count_new = count
        # elif rem == 0:
        # count = 0
        # quot = n//2
        # n = quot
        # print(count_new)
        
