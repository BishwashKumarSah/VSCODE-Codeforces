import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,lst):
    
    s = sum(lst)
    sumOfNaturalNumbers = (n*(n+1)//2)
    print(sumOfNaturalNumbers-s)
  

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    solve(n,lst)    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()