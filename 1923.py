import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    ind = -1
    for i in range(len(lst)):
        if lst[i] == 1:
            ind = i
            break
    ans = 0  
    i = ind
    j = i + 1
    while j < len(lst):
        if lst[j] == 1: 
            i += 1           
            j += 1
        elif lst[j] == 0:                 
            while j < len(lst) - 1 and lst[j] != 1:
                j += 1
            if lst[j] == 1:
                ans += (j - i) - 1
                i = j
            j += 1
               
    print(ans)

def main():
    testcases = int(input())
    while testcases > 0:
        n = int(input())        
        lst = list(map(int,input().split()))
        solve(n,lst)
        testcases -= 1
            
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()