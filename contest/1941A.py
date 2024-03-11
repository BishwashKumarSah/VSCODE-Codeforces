import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,m,k,arr1,arr2):
    arr1.sort()
    arr2.sort()
    ans = 0
    for i in arr1:
        for j in arr2:
            if i + j <= k:
                ans += 1
    print(ans)

def main():
    t = int(input())
    while t > 0:
        n,m,k = map(int,input().split())
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        solve(n,m,k,arr1,arr2)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        