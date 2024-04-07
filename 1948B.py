import sys 
from os import path

def input():
    return sys.stdin.readline().strip()


def solve(n,lst):
    arr = [lst[-1]]
    for i in range(len(lst)-2,-1,-1):     
        if lst[i] <= arr[-1]:
            arr.append(lst[i])
            continue
        else:
            
            arr.append(lst[i] % 10)
            arr.append(lst[i]//10)
    
    for i in range(1,len(arr)):
        if arr[i-1] >= arr[i]:
            continue
        else:
            print("NO")
            return
    print("YES")
    
def main():
    t= int(input())
    while t > 0 :
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        t -= 1
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()