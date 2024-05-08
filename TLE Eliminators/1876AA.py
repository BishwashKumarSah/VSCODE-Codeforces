import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,p,arr1,arr2):
    arr = list(val for val in zip(arr1,arr2))
    arr.append((n,p))
    arr.sort(key = lambda x : x[1])
    ans = p
    shared = len(arr) - 2
    i = 0    
    while shared != 0:
        if arr[i][0] <= shared:
            ans += arr[i][0] * arr[i][1]
            shared -= arr[i][0]
        else:
            ans += shared * arr[i][1]
            shared = 0
        i += 1
    print(ans)
            
    
def main():        
    t = int(input())
    for _ in range(t):
        n,p = map(int,input().split())
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        solve(n,p,arr1,arr2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()