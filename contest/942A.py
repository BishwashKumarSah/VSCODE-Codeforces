import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,arr1,arr2):
    ans = 0    
    i = 0 
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            ans += 1
            j += 1
        else:
            i += 1
            j += 1
    print(ans)
    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        solve(n,arr1,arr2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()