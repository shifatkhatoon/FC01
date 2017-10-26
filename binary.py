import sys


n = int(input().strip()
        quot = n//2
        count = 0
        count_new = 0
        while quot>0:
        rem = n%2
        if rem == 1:
        count = count + 1
        if count_new < count:
        count_new = count
        elif rem == 0:
        count = 0
        quot = n//2
        n = quot
        print(count_new)
        
