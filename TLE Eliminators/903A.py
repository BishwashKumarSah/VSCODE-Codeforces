import sys
from os import path


def input():
    return sys.stdin.readline().strip()

def solve(m,n,x,s):
    if s in x :
        print(0)
        return
    count = 0
    if len(x) > len(s):
        if s in x:
            print(0)
        else:
            x += x
            if s in x:
                print(1)
            else:
                print(-1)
        return
        
    elif len(x) == len(s) :
        if s in x:
            print(0)
            return
        if s not in x:
            x += x
            if s in x:
                print(1)
            else:
                print(-1)
        
    elif len(x) < len(s):    
        while len(x) <= 25:
            x += x
            count += 1
            if s in x:
                print(count)
                return
        print(-1)

def main():
    t = int(input())
    while t > 0:
        m,n = map(int,input().split())
        x = input()
        s = input()
        solve(m,n,x,s)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()