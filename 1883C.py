import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,k,arr):
    for i in arr:
        if i % k == 0:
            print(0)
            return
    if k != 4:
        for ind,i in enumerate(arr):
            arr[ind] = (k - (i%k))
        arr.sort()
        print(arr[0])
        return
    arr1 = arr[:]
    arr2 = arr[:]
    for ind,i in enumerate(arr):
        if i % 2 == 0:
            arr1[ind] = 0
        else:
            arr1[ind] = (2 - (i%2))
    for ind,i in enumerate(arr):
        arr2[ind] = (k - (i%k))
    arr1.sort()
    arr2.sort()
    print(min((arr1[0]+arr1[1]), arr2[0]))
        
    
            
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        solve(n,k,arr)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()