
import sys
from os import path
import math
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve(ind,w,val,N,W,lst,ans):  
    if w > W:
        return
    ans[0] = max(ans[0],val)
    for i in range(ind,len(lst)):
        w += lst[i][0]
        val += lst[i][1]
        solve(i+1,w,val,N,W,lst,ans)
        w -= lst[i][0]
        val -= lst[i][1]
        
    

def main():        
    N,W = map(int,input().split())
    lst = []
    for _ in range(N):
        val = list(map(int,input().split()))
        lst.append(val)
    lst.sort(key=lambda x : x[0])
    
    ans = [float("-inf")]
    solve(0,0,0,N,W,lst,ans)
    print(ans[0])
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()