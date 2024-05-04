import sys
import collections
import math
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve():  
    rev0 = "11101"
    rev3 = "1000001"
    if rev3 < rev0:
        print("rev3 is smaller")
        

def main():        
        
    solve()
        
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()