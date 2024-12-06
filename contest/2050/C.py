import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

def solve(val):
    lst = list(map(int,val))
    cur = sum(lst)
    if cur % 9 == 0:
        return "YES"
    
    count2 = 0
    count3 = 0
    for i in lst:
        if i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
  
    for i in range(count2+1):
        for j in range(count3+1):
            if (cur + (2*i) + (6*j)) % 9 == 0:
                return "YES"
    
    for i in range(count3+1):
        for j in range(count2+1):
            if (cur + (6*i) + (2*j)) % 9 == 0:
                return "YES"
    return "NO"
    
          
def main():
    t = int(input())
    for _ in range(t):       
        val = input()
        print(solve(val))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()