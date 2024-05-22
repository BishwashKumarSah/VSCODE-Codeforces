import sys
from os import path
import math


def input():
    return sys.stdin.readline().strip()

def solve(lst):
    
    for ind,val in enumerate(lst):
       ans = val.find("#.#")
       if ans != -1:
           print(ind+2,ans+2)
           break
           
       
       
    
            

def main():         
    for t in range(int(input())):
        input()
        lst = [input() for i in range(8)]   
        # if t == 17:
        #     print(lst)
        #     return
        solve(lst)    
        
       
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()