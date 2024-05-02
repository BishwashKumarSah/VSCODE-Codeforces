import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(s):
    i = 0
    j = 1
    ans = 0
    s = list(s)
    while j < len(s):
        if s[i] == "1" and s[j] == "0":
            ans += j - i + 1
                 
            i += 1
            s[i] ="1"
            j += 1
        elif s[i] == "1" and s[j] == "1":
            j += 1
        else:
            i += 1
            j += 1
    print(ans)
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()