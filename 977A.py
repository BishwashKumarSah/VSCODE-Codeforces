import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,k):
    st = str(n)
    while k > 0:
        if int(st[-1]) > 0:
            st = str(int(st) - 1)
        else:
            st = str(int(st)//10)
        k -= 1
    print(st)

def main():   
    n,k = map(int,input().split())
    solve(n,k)

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()