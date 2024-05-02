import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,arr):
    ans = 0
    dic = collections.Counter(arr)
    for i in dic:
        if dic[i] > 2:
            ans += dic[i] // 3
    print(ans)
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        solve(n,arr)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()