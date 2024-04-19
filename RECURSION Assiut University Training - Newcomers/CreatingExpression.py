import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(i,N,X,A,ans):
    
    if i == N:
        if ans == X:            
            return True
        return False
    
    ans += A[i]
    if solve(i+1,N,X,A,ans):
        return True        
    ans -= A[i]
    
    ans -= A[i]
    if solve(i+1,N,X,A,ans):
        return True        
    ans += A[i]
    return False
    

def main():        
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    
    if solve(1,N,X,A,A[0]):
        print("YES")
        return
    print("NO")
    return

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()