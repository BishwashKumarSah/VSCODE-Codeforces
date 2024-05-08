import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,k,arr):
    arr = [[val,ind+1] for ind,val in enumerate(arr)]
    for i in arr:
        if i[0] % k == 0:
            i[0] = k
        else:
            i[0] = i[0] % k
    
    arr.sort(key = lambda x : x[1])         
    arr.sort(key = lambda x : x[0],reverse = True)
    for i in arr:
        print(i[1],end=" ")   
    
            
    
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