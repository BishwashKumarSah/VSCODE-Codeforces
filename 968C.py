import sys
from os import path
import math
from collections import *



def input():
    return sys.stdin.readline().strip()


def solve(n, s):
    dic = Counter(s)
    res = ""
    while dic:
        
        for i in dic:
            if dic[i] != 0:
                res += i
                dic[i] -= 1
        val = sum(dic.values())
        if val == 0:
            print(res)
            return
        
            
                
    print(res)
    
        
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n, s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()