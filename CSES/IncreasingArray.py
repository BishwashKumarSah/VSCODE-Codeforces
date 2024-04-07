import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,lst):
    ans = 0
    for i in range(1,n):
        if lst[i] >= lst[i-1]:
            continue
        else:
            diff = lst[i-1] - lst[i]
            ans += diff
            lst[i] += diff
    print(ans)    

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    solve(n,lst)    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()