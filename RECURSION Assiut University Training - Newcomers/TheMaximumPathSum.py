import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(r,c,R,C,matrix,ans,val):
    if r == R:
        return
    if c == C:
        return
    val += matrix[r][c]
    ans[0] = max(ans[0],val) 
    solve(r+1,c,R,C,matrix,ans,val)
    solve(r,c+1,R,C,matrix,ans,val)
    val -= matrix[r][c]

def main():        
    
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    ans = [float("-inf")]
    solve(0,0,N,M,matrix,ans,0)
    print(ans[0])

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()