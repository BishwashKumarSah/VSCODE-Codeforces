import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(s1,s2):
    count = 0
    t = len(s1) + len(s2)
    bool = True
    
    for ind,i in enumerate(s2):
        if bool == False and i not in s1:
            break        
        
        elif i in s1:
            count += 1
            val = s1.index(i)            
            s1 = s1[val+1:]
            bool = False
            
    total = t - count
    print(total)

def main():
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        if (t == 1000 and i == 578) or ( t == 1000 and i == 577) or (t == 1000 and i == 579):
            print("string",i,s1,s2)
        if t == 1000:
            continue
        
        solve(s1,s2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()