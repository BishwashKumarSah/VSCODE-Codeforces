import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()


def solve(n, lst):
    max_element = max(lst)
    ind = lst.index(max_element)
    
    if len(lst) <= 2:
        print(-1)
        return
    
    avg = (sum(lst)/len(lst))/2
    count = 0
    for i in lst:
        if i < avg:
            count += 1
    if count > len(lst)/2:
        print(0)
        return
    
    low = 0
    high = 2**63 - 1
    
    def canAddGold(target):
        lst[ind] += target
        avg = (sum(lst)/len(lst))/2
        count = 0
        for i in lst:
            if i < avg:
                count += 1
        if count > len(lst)/2:
            lst[ind] -= target
            return True
        lst[ind] -= target
        return False
        
    def bs(low,high):
        while high - low > 1:
            mid = low + (high - low)//2
            if canAddGold(mid):
                high = mid
            else:
                low = mid + 1
        if canAddGold(low):
            print(low)
            return
        elif canAddGold(high):
            print(high)
            return
        else:
            print(-1)
            return
    bs(low,high)
                

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