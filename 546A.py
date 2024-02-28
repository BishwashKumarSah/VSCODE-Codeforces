import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(k,n,w):
    cost = (w * (w + 1)//2) * k
    if cost <= n:
        print(0)
        return
    borrow = cost - n
    print(borrow)

def main():
    k,n,w = map(int,input().split())
    solve(k,n,w)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()