import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,s):
    ans =""
    
    if s > s[::-1]:
        ans += s[::-1]
        ans += s[::]
    else:
        ans += s[::]
    print(ans)

def main():
    testcases = int(input())
    while testcases > 0:
        n = int(input())        
        s= input()
        solve(n,s)
        testcases -= 1
            
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()