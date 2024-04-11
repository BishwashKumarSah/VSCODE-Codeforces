import sys
from os import path
import math
import decimal

def input():
    return sys.stdin.readline().strip()

def solve():
    

    print(2**2*(10**5))

    
    
    
def main():
    # cook your dish here
    
    solve()
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()