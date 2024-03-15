import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n):
    ans = ""
    if n <= 1 or n % 2 != 0:
        print("NO")
        return
    while n > 0:
        ans += "AA"
        ans += "B"
        n -= 2
    print("YES")
    print(ans)
    
    

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        solve(n)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        