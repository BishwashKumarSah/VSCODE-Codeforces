import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,lst):
    lst.sort()
    i = lst[0]
    k =  lst[1]
    j = lst[-2]
    l = lst[-1]
    print(abs(i-j)+abs(j-k)+abs(k-l)+abs(l-i))
  

def main():
    t = int(input())  
    while t > 0:
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        t -= 1
    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()