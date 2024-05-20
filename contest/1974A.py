import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,s):
    distn = sorted(set(s))
    r = ''.join(distn)    
    char_map = {}
    n = len(r)
    for i in range(n):
        char_map[r[i]] = r[n -1-i]  
    print(char_map)  
    enc = ''.join(char_map[char] for char in s)    
    print(enc) 
    
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n,s)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()