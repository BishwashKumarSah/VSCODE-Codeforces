import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(x,y):
    
    if y == 0:
        print(math.ceil(x/15))
        return
    elif x == 0:
        print(math.ceil(y/2))
        return
    
    y_valCeil = math.ceil(y/2)
    y_valInt = y//2
    total_area = (15*y_valCeil)
    remaining = (total_area - (4*y))
    
    if x > remaining:
        x = x - remaining
        print(y_valCeil + math.ceil(x/15))
    else:
        print(y_valCeil)    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        solve(x,y)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()