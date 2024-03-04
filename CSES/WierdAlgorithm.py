import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n):
    if n == 1:
        print(1)
        return 
    print(n,end=" ")
    while n != 1:    
            
        if n % 2 == 0:
            n = n//2
        else:
            n = (n*3) + 1
        print(n,end=" ")
  

def main():
    n = int(input())
    solve(n)    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()