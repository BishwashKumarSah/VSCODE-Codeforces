import sys
from os import path


def input():
    return sys.stdin.readline().strip()

def solve(n):
    if (n - 1) % 3 == 0 or (n+1) % 3 == 0:
        print("First")
    else:
        print("Second")
    
def main():
    t = int(input())
    while t > 0:
        n = int(input())
       
        solve(n)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()