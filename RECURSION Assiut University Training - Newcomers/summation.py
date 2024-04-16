import sys
from os import path
import sys,threading
sys.setrecursionlimit(10009)
# threading.stack_size(10**4)
def input():
    return sys.stdin.readline().strip()

def solve(i,n,lst,ans):
    if i == n:
        print(ans)
        return
    ans += lst[i]
    solve(i+1,n,lst,ans)
    
        
def main():
    n = int(input())
    lst = list(map(int,input().split()))
    solve(0,n,lst,0)  
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()