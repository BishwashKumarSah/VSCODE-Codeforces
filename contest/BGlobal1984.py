import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,lst):
    c = 0
    
    for i in range(n):
        if c + lst[i] >= 0:
            c += lst[i]
        else:
            c = abs(c + lst[i])
    import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,lst):
    def recu(i,lst,c):
       if i == len(lst):
           return c
       val1 = recu(i+1,lst,c+lst[i])
       val2 = recu(i+1,lst,abs(c+lst[i]))
       return max(val1,val2)
    ans= recu(0,lst,0)
    print(ans)
        
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
    
        
    
 