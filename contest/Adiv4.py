import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(r,c,arr):
    res = []
    for i in range(len(arr)):
        co = 0
        a = arr[i]        
        for c in a:
            if c == "#":
                co += 1
        res.append(co)
    # print(res)
    lst = [1,1]
    m = res[0]
    
    for i in range(1,len(res)):
        if res[i] >= res[i-1]:
            m = res[i]
            lst[0] = i+1
        else:
            break
    # print(lst)
    if m == 1:
        array = arr[lst[0]-1]        
        for j in range(len(array)):
            if array[j] == "#":
                lst[1] = j + 1
                break
        print(*lst)
    else:
        lst[1] = math.ceil(m/2)
        array = arr[lst[0]-1]     
        cc = 0   
        for j in range(len(array)):
            if array[j] == "#":
                cc += 1
                if cc == lst[1]:
                    lst[1] = j+1
                
                    break
        
        print(*lst)
        
        
        
        
    
            
    
        
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        r,c = map(int,input().split())
        arr = [input() for _ in range(r)]               
        solve(r,c,arr)
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()