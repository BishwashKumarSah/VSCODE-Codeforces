import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n):
    even = []
    odd = []
    not_any = []
    common = []
    for i in range(1,n+1):
        if i % 2 == 0 and i % 3 == 0:
            common.append(i)
        elif i % 2 == 0:
            even.append(i)
        elif i % 3 == 0:
            odd.append(i)
        else:
            not_any.append(i)
    if n <= 4:
        print(-1)
        return 
    lst = []
    
    if n == 5:
        print(*[2, 4, 5, 1, 3 ])
        return
        
    
    for i in not_any:
        lst.append(i)
    for i in odd:
        lst.append(i)
    for i in common:
        lst.append(i)
    for i in even[::-1]:
        lst.append(i)
 
    print(*lst)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())        
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()