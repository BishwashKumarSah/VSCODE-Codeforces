import sys
from os import path
import math
import collections

def input():
    return sys.stdin.readline().strip()


def solve(n,lst):
    dic = collections.defaultdict(list)
    
    for s in lst:
        if s not in dic:
            print("OK")
            dic[s].append(0)
        else:    

            dic[s].append(dic[s][-1]+1)
            print(s+str(dic[s][-1]))
    

def main():
    n = int(input())
    lst = []
    while n > 0:
        lst.append(input())
        n -= 1
    solve(n,lst)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()