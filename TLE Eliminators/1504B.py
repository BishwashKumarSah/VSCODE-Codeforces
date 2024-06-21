import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, A, B):
    lst = []
    lst2 = []
    count0 = 0
    count1 = 0
    s = ""    
    s2 = ""
    for i in range(0,len(A)):
        s += A[i]
        s2 += B[i]
        if A[i] == "0":
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:            
            count0 = 0
            count1 = 0            
            lst.append(s)
            lst2.append(s2)
            s = ""
            s2 = ""
    
    if len(s) > 0:
        if s != s2:
            print("NO")
            return

        
    for ind,val in enumerate(lst):
        count = 0
        for ch in range(len(val)):
            if lst[ind][ch] != lst2[ind][ch]:
                count += 1
        if count == 0 or count == len(lst[ind]):
            continue
        else:
            print("NO")
            return
    print("YES")
   

def main():
    t = int(input())
    for tt in range(t):
        n = int(input())
        s1 = input()
        s2 = input()
        solve(n, s1, s2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()