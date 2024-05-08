import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,lst):
    lst.sort(key = lambda x : x[1],reverse = True)
    res = float("inf")
    ans = 0
    for i in range(len(lst)-1):
        res = min(res,lst[i][0])
        ans += lst[i][1]
    ans += min(lst[-1][0],res)
    print(ans)    
            
    
def main():        
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = []
        for _ in range(n):
            m = int(input())
            arr = list(map(int,input().split()))
            arr.sort()
            lst.append(arr)
        
        solve(n,lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()