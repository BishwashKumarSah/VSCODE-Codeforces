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
    
    
    target = total_sum // n
    
    
    diff = [lst[i] - target for i in range(n)]
    
    
    total_shift_performed = 0
    for d in diff:
        total_shift_performed += d
        
        if total_shift_performed < 0:
            print("NO")
            return
    
    print("YES")

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