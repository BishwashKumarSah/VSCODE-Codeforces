import sys
from os import path
def input():
    return sys.stdin.readline().strip()

    
def solve(n,s):
    # YOUR CODE HERE    
    ans = 0
    i = 1
    while i < n:
        if s[i] == "@":
            ans += 1
            i += 1 
        elif s[i] == ".":
            i += 1           
        elif s[i] == "*": 
            if i == n-1 or s[i+1] == "*":
                print(ans)
                return
            else:
                i += 1
        
    print(ans)       
            
        
            
    

def main():
    # testcases = 1 
    
    testcases = int(input()) # multiple testcases
    for _ in range(testcases):
        n = int(input())
        s = input()
        solve(n,s)
        

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()