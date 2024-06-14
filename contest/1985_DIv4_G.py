import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(l,r,k):
    ans = 0
    def sum_of_digits(n):
        s = 0
        while n > 0:
            s += n%10
            n = n//10            
        return s
    for i in range(10**l,(10**r)):  
        if i % 1 == 0 or i %2 == 0 or i % 3 == 0 or i % 4 == 0:
            if sum_of_digits(k*i) == k * sum_of_digits(i):
                ans += 1
    print(ans)
            
        
    
def main():
    t = int(input())
    for _ in range(t):
        l,r,k = map(int,input().split())          
        solve(l,r,k)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()