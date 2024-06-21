# link :https://leetcode.com/discuss/interview-experience/5341224/stripe-backend-engineer-bangalore-jun-2024-reject
import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(s):
    opening = -1
    closing = -1
    for ind,val in enumerate(s):
        if val == "{":
            if opening == -1:
                opening = ind
        if val == "}":
            if closing == -1:
                closing = ind + 1
    right = s[0:opening]
    left = s[closing:]
    mid = s[opening+1:closing-1]    
    mid = mid.split(",")
    for i in mid:
        val = right + i + left
        print(val)
    

def main():
    t = int(input())
    for _ in range(t):
       s = input()
       solve(s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()