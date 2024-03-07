import sys
from os import path


def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    for i in range(1,len(lst)):
       if lst[0] > lst[i]:
           print("NO")
           return
    
    print("YES")
    
    
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()