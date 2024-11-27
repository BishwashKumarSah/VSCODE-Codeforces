import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, k):
    if n == 1 or k == 1:
        print(-1)
        return
    lst = []
    for i in range(1,n+1):        lst.append(i)
        
    new_lst = []
    for i in range(1,n+1):        new_lst.append(i % k)
    
    n2 = []
    for i in range(1,n+1):        n2.append(i%k)

    for i in range(n):
        if new_lst[i] == n2[i]:
            if i + 1 < n:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                new_lst[i],new_lst[i+1] = new_lst[i+1],new_lst[i]
            else:
                lst[i],lst[i-1] = lst[i-1],lst[i]
                new_lst[i],new_lst[i-1] = new_lst[i-1],new_lst[i]
    dic = set()
    for i in lst:
        if i in dic:
            print(-1)
            return 
        dic.add(i)
    print(*lst)
   

def main():
    t = int(input())
    for _ in range(t):
        n,k = (map(int, input().split()))
        
        solve(n, k)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()