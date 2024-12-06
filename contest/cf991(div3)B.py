import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()



def solve(n,lst):   
    total_sum = 0
    for i in lst:
        total_sum += i    
    
   
    if total_sum % n != 0:
        print("NO")
        return 
    
    
    oddCount = 0
    evenCount = 0
    evenVal = 0
    oddVal = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            evenCount += 1
            evenVal += lst[i]
        else:
            oddCount += 1
            oddVal += lst[i]
    avgEven = evenVal/evenCount
    avgOdd = oddVal/oddCount
    if avgEven == avgOdd:
        print("YES")
        return
    print("NO")
        
    
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        solve(n, lst)
        

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()