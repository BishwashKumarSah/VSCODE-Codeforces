import sys 
from os import path
from math import comb
def input():
    return sys.stdin.readline().strip()
 
def solve(n,lst):
    ans = [0] * len(lst)
    dic = {}
    for i in range(len(lst)):
        ans[i] = lst[i] - (i+1)

    for i in ans:
        dic[i] = 1 + dic.get(i,0)
        
    res = 0
    for i in dic:
        if dic[i] > 1:
            res += comb(dic[i],2)
    print(res)

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