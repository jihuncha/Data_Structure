temp = [0,0,0,0,1,1,0,1]

import bisect
print(temp[3:])
print(bisect.bisect_left(temp[3:],0))
print(bisect.bisect_right(temp[3:],0))

print(set(temp))

if len(set(temp)) == 1:
    print("test")

if list(set(temp))[0] == 0:
    print("fdsafa")