import collections
t = int(input())
for _ in range(t):
    
    val = input()
    dic = collections.Counter(val)
    
    m = max(dic.values())
    
    if m == 4:
        print(-1)
    elif m == 3:
        print(6)
    elif m == 2 or m == 1:
        print(4)
    