import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(s):
    res = float("-inf")
    i,j = 0,0
    
    while j < len(s):
        if s[j] == s[i]:
            res = max(res, j - i + 1)
            j += 1
        else:
            
            i = j
    print(res)
        

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    solve(n.lst)    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()