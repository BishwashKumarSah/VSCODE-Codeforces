import sys
from os import path
import collections

def input():
    return sys.stdin.readline().strip()


def solve(n, s):
    
    left = set(s[0])
    right = collections.Counter(s[1:])
    res = len(left) + len(right)
    for i in range(1,len(s)-1):
        left.add(s[i])
        right[s[i]] -= 1
        if right[s[i]] == 0:
            del right[s[i]]
        res = max(res,len(left)+len(right))
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