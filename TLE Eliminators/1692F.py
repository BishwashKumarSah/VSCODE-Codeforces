import sys
from os import path
import math


def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    res = []
    dic = {}
    for i in lst:
        val = i % 10
        
        if val in dic:
            if dic[val] == 3:
                continue   
            else:
                res.append(val)
                dic[val] += 1
        else:
            dic[val] = 1 
            res.append(val)
    for i in range(len(res)):
        for j in range(i+1,len(res)):
            for k in range(j+1,len(res)):
                if (res[i] + res[j] + res[k]) % 10 == 3:
                    print("YES")
                    return
    print("NO")
    
        
    

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