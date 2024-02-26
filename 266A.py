import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,s):
    ans = 0
    for i in range(0,n-1):
        if s[i] == s[i+1]:
            ans += 1
        
    print(ans)

def main():    
    n = int(input())
    s = input()
    solve(n,s)

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()