import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,m,s):
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    dic1 = collections.Counter(s)
    ans = 0
    
    for i in lst:
        if i not in dic1:
            ans += m
        else:
            if dic1[i] >= m:
                continue
            ans += abs(dic1[i]-m)       
        
    print(ans)
    
   
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        s = input()
        solve(x,y,s)
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()