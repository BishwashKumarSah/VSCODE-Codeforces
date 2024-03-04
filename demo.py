import sys 
from os import path

def input():
    return sys.stdin.readline().strip()


def solve(lst):
    lst.sort()
    print(lst)
    maxEle = lst[-1]
    i,j = 0,0
    val = 0
    while j < len(lst):
        val += lst[j]
        if val < maxEle:
            j += 1
        else:
            if val == maxEle:
                print(lst[i:j+1])
                return
            while val > maxEle:               
                val -= lst[i]
                i += 1
                if val == maxEle:
                    print(lst[i:j+1])
                    return

def main():
    lst = list(map(int,input().split()))
    solve(lst)
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()