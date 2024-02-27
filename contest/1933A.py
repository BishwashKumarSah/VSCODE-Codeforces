import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,k):
    s = 0
    for i in k:
        if i < 0:
            s += -1 * i
        else:
            s += i
    print(s)

def main():
    t = int(input())  
    while t > 0:
        n = int(input())
        k = list(map(int,input().split()))
        solve(n,k)
        t -= 1
    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()