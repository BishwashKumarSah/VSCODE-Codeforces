import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(l, r , n, arr, target):
    if l > r:
        return -1
    mid = l - (l - r)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return solve(mid+1,r,n,arr,target)
    else:
        return solve(l, mid+1, n, arr, target)

def main():        
    n = int(input())
    target = int(input())
    arr = list(map(int,input().split()))    
    ans = solve(0,n - 1, n, arr, target)
    print(ans)        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()