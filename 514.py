import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(a):
    d = str(a)

    modified_number = ""
    for s in range(len(d)):
        if s == 0 and d[s] == "9":
            modified_number += d[s]
        elif int(d[s]) > 4:            
            modified_number += str(9 - int(d[s]))
        else:
            modified_number += d[s]    
    
    if modified_number:
        print(int(modified_number))
    else:
        print(int(modified_number))
    
    

def main():
    a = int(input())
    solve(a)
    
if __name__ == "__main__":
    if(path.exists("input.txt")):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()