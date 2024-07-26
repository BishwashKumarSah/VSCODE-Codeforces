import sys
from os import path
import math
from collections import *
import heapq


def input():
    return sys.stdin.readline().strip()


def solve(n,k,a,b):  
    heap = [(-element, index) for index, element in enumerate(a)]   
    heapq.heapify(heap)
    ans = 0
    while k > 0:
        val = list(heapq.heappop(heap))
        if val[0] ==0:
            print(ans)
            return
        data = abs(val[0]) 
        ans += data
        val[0]  = max(0,abs(val[0]) - b[val[1]] )   * -1   
        heapq.heappush(heap,tuple(val))
        k -= 1
    print(ans)
        
    

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, k,a,b)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()