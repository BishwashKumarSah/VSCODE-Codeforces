import sys
import collections
import math

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,k,b,s,p,a):
    ans = [0,0]
    lst = [b-1,s-1]
    kk = k
    for ind,i in enumerate(lst):
        j = i
        flag = True
        k = kk
        while flag:                     
            if p[j] - 1 == j:
                ans[ind] = k * a[j]
                print("sfd")
                flag = False
            else:            
                
                res = k * a[j]                               
                val = a[j]
                x = j   
                k -= 1           
                while k > 0:
                    x = p[x] - 1
                    val += a[x]
                    k -= 1
                ans[ind] = max(res,val)
                flag = False
    print(ans)
    if ans[0] > ans[1]:
        print("Bodya")
    elif ans[0] < ans[1]:
        print("Sasha")
    else:
        print("Draw")
def main():        
    t = int(input())
    for _ in range(t):
        n,k,b,s = map(int,input().split())
        p = list(map(int,input().split()))
        a = list(map(int,input().split()))
        solve(n,k,b,s,p,a)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()