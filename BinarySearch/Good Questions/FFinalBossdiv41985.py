import sys
from os import path
import math

def input():
    return sys.stdin.readline().strip()

def solve(h,n,attack,cooldown):
    val = sum(attack)
    
    if val >= h:
        print(1)
        return
    
    def check(m):
        
        total_pow = 0
        for i in range(len(attack)):
            no_of_times_attack = math.ceil(m/cooldown[i])
            total_pow += attack[i] * no_of_times_attack
        if total_pow >= h:
            return True
        return False
            
        
    def bs(low,high):
        while high - low > 1:
            mid = low + (high-low)//2
            if check(mid):
               
                high = mid
            else:
                low = mid + 1
        if check(low):
            print(low)
            return
        print(high)
        return
    bs(1,4*10**11)
            
    
def main():
    t = int(input())
    for _ in range(t):
        h,n = map(int,input().split())
        attack = list(map(int,input().split()))
        cooldown = list(map(int,input().split()))  
        solve(h,n,attack,cooldown)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()