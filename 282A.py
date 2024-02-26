import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(lst):
    c = 0
    for i in lst:            
        if "++" in i:
            c += 1
        elif "--" in i:
            c -= 1
    print(c)
    

def main():
    testcases = int(input())
    lst = []
    for _ in range(testcases):
        s = input()
        lst.append(s) 
    solve(lst)

if __name__ == "__main__":
    if (path.exists("input.txt")):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        