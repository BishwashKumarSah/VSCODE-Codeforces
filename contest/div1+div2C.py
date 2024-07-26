import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    stack = []
    ans = 0
    for i in range(len(lst)):
        
        if stack and stack[0] >= lst[i]:
            if lst[i] == stack[0]:
                stack.append(lst[i])
            
        else:       
           
            if stack:   
                if lst[i] > stack[0]:
                    ans += sum(stack) 
                    stack = []                   
                    
                else:
                    ans += len(stack) 
                    stack = []
        stack.append(lst[i])
   
    if stack:
        if len(stack) > 1:
            ans += stack[0] + len(stack)
        else:
            ans += stack[0]
    print(ans)       
            

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