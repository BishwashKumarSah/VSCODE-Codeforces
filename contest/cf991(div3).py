import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

def solve(val):
    lst = list(map(int,val))
    
    cur_sum = sum(lst)
    if cur_sum % 9 == 0:
        return "YES"
    cache = {}
    def recu(ind,cur_sum):
        if ind >= len(lst):
            if cur_sum % 9 == 0:
                return True
            return False
        if (ind,cur_sum) in cache:
            return cache[(ind,cur_sum)]
        if cur_sum % 9 == 0:
            return True
        res = recu(ind+1,cur_sum)
        if lst[ind] == 2:
            res = res or recu(ind+1,cur_sum + 2)
        if lst[ind] == 3:
            res = res or recu(ind+1,cur_sum+6)
        cache[(ind,cur_sum)] = res
        return cache[(ind,cur_sum)]
    if recu(0,cur_sum):
        return "YES"
    return "NO"        
def main():
    t = int(input())
    for _ in range(t):       
        val = input()
        print(solve(val))

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()