import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def default_factory():
    return []

def solve(n,lst):
    
    dic = collections.defaultdict(default_factory)   
    for i in range(len(lst) - 2):
        arr = [lst[i],lst[i+1],lst[i+2]]
        a1 = (0,arr[1],arr[2])
        a2 = (arr[0],0,arr[2])
        a3 = (arr[0],arr[1],0)
        dic[a1].append(arr[0])
        dic[a2].append(arr[1])
        dic[a3].append(arr[2])
    # print(dic)
    ans = 0
    for val in dic:       
        if len(set(dic[val])) >= 2:
            # print(dic[val])            
            d = collections.Counter(dic[val]) 
            total = len(dic[val])
            for i in dic[val]:
                ans += total - d[i]            
    print(ans//2)

def main():        
    t = int(input())
    for _ in range(t):
       n = int(input())
       lst = list(map(int,input().split()))
       solve(n,lst)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()