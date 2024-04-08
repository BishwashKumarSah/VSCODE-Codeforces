import sys
from os import path
import math
import collections

def input():
    return sys.stdin.readline().strip()

def solve(n,k,lst):
    ans = collections.deque(lst)
    res = 0
    if k%2==0:
        k1 = k//2 
        k2 = k//2
    else:
        k1 = k//2 + 1
        k2 = k//2
    
    while k > 0 and  ans:
        if k2 == 0 and k1 == 0:
            print(res)
            return
            
        if k > 0 and  k1 > 0 and ans[0] <= k1:
            k1 -= ans[0]
            if k1 == 0:
                k -= k1
            res += 1
            ans.popleft()
            
        else:            
            
            ans[0] -= k1
            k1 = 0

        if k > 0 and k2 > 0 and ans :
            if ans[-1] <= k2:
                k2 -= ans[-1]
                if k2 == 0:
                    k -= k2
                res += 1
                ans.pop()
            else:            
                ans[-1] -= k2
                k2 = 0
         
    print(res)

def main():
    t = int(input())
    while t > 0:
        n,k = list(map(int,input().split()))
        lst = list(map(int,input().split()))
        solve(n,k,lst)
        t -= 1
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()