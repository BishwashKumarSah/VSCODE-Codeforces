import sys
from os import path
import math
import string
from collections import *
from itertools import product

def input():
    return sys.stdin.readline().strip()


def solve(n, s):
    import string

def solve(n, s):
    length = 1
    a = [1,2,3]
    b = [2,4,5]
    print(list(product(a,b)))
    while True:
        for comb in product(string.ascii_lowercase,repeat=length):
            
            combination = "".join(comb)
            
            if combination not in s:
                print(combination)
                return
        length += 1
        


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