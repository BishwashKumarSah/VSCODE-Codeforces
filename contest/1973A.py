import sys
from os import path
import heapq

def input():
    return  sys.stdin.readline().rstrip("\r\n")    

def solve(p1,p2,p3): 
    lst = []
    
    if (p1+p2+p3)%2 != 0 :
        print(-1)
        return
    if p1 != 0:
        heapq.heappush(lst,-1* p1)
    if p2 != 0:
        heapq.heappush(lst,-1* p2)
    if p3 != 0:
        heapq.heappush(lst,-1* p3)
    if len(lst) == 0:
        print(0)
        return 
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            print(0)
            return
        else:
            print(-1)
            return
    
    
    ans = 0
    
    while len(lst) > 1:
        val1 = abs(heapq.heappop(lst))
        val2 = abs(heapq.heappop(lst))
        val1 -= 1
        val2 -= 1
        ans += 1
        if val1 > 0:            
            heapq.heappush(lst,-1*val1)
        if val2 > 0:
            heapq.heappush(lst,-1*val2)
    print(ans)
    

def main():   
    t = int(input())  
    for _ in range(t):
        p1,p2,p3 = map(int,input().split())
        solve(p1,p2,p3)
        
    
            
    

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()