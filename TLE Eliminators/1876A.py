import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,p,arr1,arr2):
    new_arr = list(zip(arr1,arr2))
    new_arr.append([len(new_arr)+1,p])
    new_arr = [list(val) for val in new_arr]
    new_arr.sort(key=lambda x:x[0],reverse=True)
    new_arr.sort(key=lambda x : x[1])
    ans = p
    shared = 2
    remaining = len(new_arr) - 2
    p = 0
    while shared != (len(new_arr)):
        if new_arr[p][0] >= remaining:
            ans += (remaining * new_arr[p][1])
            print(ans)
            return
        else:
            remaining = remaining - new_arr[p][0]
            ans += new_arr[p][0] * new_arr[p][1]
        
        p += 1
    
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