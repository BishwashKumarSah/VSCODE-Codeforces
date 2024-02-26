import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,t,s):
    while t > 0:
        s = s.replace("BG","GB")
        t -= 1
    print(s)

def main():    
    n,t = map(int,input().split())
    s = input()
    solve(n,t,s)

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()