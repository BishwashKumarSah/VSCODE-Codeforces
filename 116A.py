import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    prev = lst[0][1]
    ans = lst[0][1]
    for i in range(1,len(lst)):
        prev = prev + lst[i][1] - lst[i][0]
        ans = max(ans,prev)
    print(ans)

def main():
    n = int(input())
    lst = []
    while n > 0:
        l = list(map(int,input().split()))
        lst.append(l)
        n -= 1
    solve(n,lst)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()