import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,arr,target):
    low = 0 
    high = len(arr) - 1
    while high - low > 1:
        mid = low + (high - low)//2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    if arr[low] >= target:
        print(low)
    elif arr[high] >= target:
        print(high)
    else:
        if target > arr[high]:
            print(high)   
        else:
            print(low)
    
def main():        
    n = int(input())
    target = int(input())
    arr = list(map(int,input().split()))      
    solve(n,arr,target)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()