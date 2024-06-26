import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

Prime = [False for _ in range(200007)] 
def prime():        
    for i in range(2,len(Prime)):
        if Prime[i] == True:
            continue
        for j in range(i*i,len(Prime),i):
            Prime[j] = True 
                
def solve(n, lst):
    dic = Counter(lst)
    if 1 not in dic:
        print(*lst)
        return
    pre = 1
    res = [1]
    dic[1] -= 1    
    for i in range(1,len(lst)):
        if Prime[pre + 1] == False and dic[1] > 0:
            dic[1] -= 1            
            res.append(1)
            pre += 1
        elif Prime[pre + 2] == False and dic[2] > 0:
            dic[2] -= 1
            res.append(2)
            pre += 2
        else:
            if dic[2] > 0:
                pre += 2
                dic[2] -= 1
                res.append(2)
            else:
                pre += 1
                dic[1] -= 1
                res.append(1)
    print(*res)
    
    

def main():           
    prime()     
    n = int(input())
    lst = list(map(int, input().split()))
    solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()