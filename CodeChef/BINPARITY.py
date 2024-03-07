import sys
from os import path


def input():
    return sys.stdin.readline().strip()

def solve(n):
    s = bin(n)[2:]
    c = s.count("1")
    if c % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
    
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