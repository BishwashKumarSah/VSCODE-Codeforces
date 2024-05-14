import sys
import collections
import math
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,lst): 
    ans = lst[2:n+2]
    print(len(set(ans)))
    print(*ans)
    
    
def main():   
    lst = [1] * 100002
    for i in range(2,len(lst)):
        if lst[i] == 1:
            for j in range(i*2,len(lst),i):                
                if lst[j] >1:
                    continue
                lst[j] += 1
     
    n = int(input())
    solve(n,lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()