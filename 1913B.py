import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(s):
    count0 = 0
    count1 = 0
    s = list(s)
    for i in s:
        if i == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 == count1:
        print(0)
        return
    t = s[:]
    
    for ind,val in enumerate(s):
        if t[ind] == "1" and count0 > 0:
            t[ind] = "0"
            count0 -= 1
            
        elif t[ind] == "0" and count1 > 0:
            t[ind] = "1"
            count1 -= 1
    ans = 0
    
    for ind,val in enumerate(s):
        if s[ind] != t[ind]:
            continue
        j = ind
        while j < len(t) and s[ind] == t[j]:
            ans += 1
            j += 1
        if j == len(t):
            print(ans)
            return
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