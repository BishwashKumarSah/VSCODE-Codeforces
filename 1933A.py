import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,k):
    s = sum(k)
    if s % 3 == 0:
        print(0)
        return
    remainder = s % 3
    lst = [x%3 for x in k ]
    if remainder == 1:
        if 1 in lst:
            print(1)
            return
        else:
            print(2)
    
    if  remainder == 2:
        if 2 in lst:
            print(1)
            return
        else:
            print(1)
    
            
    
                
        
   

def main():
    t = int(input())  
    while t > 0:
        n = int(input())
        k = list(map(int,input().split()))
        solve(n,k)
        t -= 1
    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()