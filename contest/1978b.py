import sys
from os import path
import math
import collections

def input():
    return sys.stdin.readline().strip()

def bs(low,high,a,b):
        while high - low > 1:
            mid = low + (high - low) //2
            if b - mid  < a:
                high = mid - 1
            else:
                low = mid
        
        if b - high >= a:
            return high
        if b - low >= a:
            return low
        return -1
def solve(n,a,b):
    val = bs(0,n-1,a,b)
    if val == -1:
        print(n * a)
    else:        
        discount = ((val+1) * b ) - ((val*(val+1))//2)        
        remaining = n - (val + 1)
        total = discount + (remaining * a) 
        print(total)
    
    
            
    

def main():
    t = int(input())
    for _ in range(t):
        n,a,b = map(int,input().split())
        solve(n,a,b)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()