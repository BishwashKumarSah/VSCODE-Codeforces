import sys
import collections
import math 
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(n,f,k,lst):
    fav = lst[f-1]
    lst.sort(reverse=True)
    # print(lst)
    flag = False
    i = 0
    while i < k:
        if lst[i] == fav:            
            flag = True            
             
        i += 1           
    # print(i)       
    if flag == True:
        if i  < len(lst) and lst[i] == fav:
            print("MAYBE")
        else:
            print("YES")
    else:
        print("NO")      
   
    
    
    
def main():        
    t = int(input())
    for _ in range(t):
        n,f,k = map(int,input().split())
        lst = list(map(int,input().split()))
        solve(n,f,k,lst)
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()