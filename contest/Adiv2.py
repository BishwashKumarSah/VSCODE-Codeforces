import sys
from os import path
import math
from functools import reduce

def input():
    return sys.stdin.readline().strip()

def lcm(a, b):
    return math.lcm(a, b)

def solve(n):
    lst = []
    for i in range(n):
        s = set()
        s.add(i + 1)
        lst.append(s)

    for i in range(n): 
        for j in range((i + 1) * 2, n + 1, i + 1):
            lst[j - 1].add(i + 1)
    
    res = [0] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        numbers = list(lst[i])
        overall_lcm = reduce(lcm, numbers)
        for num in numbers:
            res[num - 1] += overall_lcm
    
    print(*res)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())        
        solve(n)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()
