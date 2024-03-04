import sys 
from os import path

def input():
    return sys.stdin.readline().strip()


def solve(s):
    lst = s.split()
    ind = [0,0]
    dic = {}    
    for m in range(len(lst)):
        dic = set()
        i = 0
        for c in lst[m]:
            if c not in dic:
                dic.add(c)
            else:
                i += 1
        if i > ind[0]:
            ind[0] = i
            ind[1] = m
        
    print(lst[ind[1]])    
        
        
def main():
    s = input()
    solve(s)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()