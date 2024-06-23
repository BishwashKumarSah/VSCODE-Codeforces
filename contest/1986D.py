import sys
from os import path
import math
from collections import *

 

def input():
    return sys.stdin.readline().strip()

def solve(n, s):
    if n - 2 == 0:
        print(int(s))
        return
    memo = {}        
    def min_result(i, ops_left):
        if (i, ops_left) in memo:
            return memo[(i, ops_left)]        
        if ops_left == 0:
            result = int(s[i:])
            memo[(i, ops_left)] = result
            return result        
        min_val = float('inf')
        for j in range(i + 1, len(s)):
            left_num = int(s[i:j])            
            result_mul = left_num * min_result(j, ops_left - 1)            
            result_add = left_num + min_result(j, ops_left - 1)            
            min_val = min(min_val, result_mul, result_add)        
        memo[(i, ops_left)] = min_val
        return min_val    
    min_result_for_case = min_result(0, n - 2)
    print(min_result_for_case)

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