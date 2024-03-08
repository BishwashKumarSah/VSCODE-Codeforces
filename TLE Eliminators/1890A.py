import sys
from os import path


def input():
    return sys.stdin.readline().strip()

def solve(n,lst):
    dic = {}
    for i in lst:
        dic[i] = 1 + dic.get(i,0)
    if len(dic) == 1:
        print("YES")
        return
    if len(dic) > 2:
        print("NO")
        return 
    c = 0
    if len(lst) % 2 == 0:
        c = len(lst)//2
    else:
        c = len(lst)//2 + 1
        
    for i in dic:
        if dic[i] == c:
            print("YES")
            return
    print("NO")
    
    
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        lst = list(map(int,input().split()))
        solve(n,lst)
        t -= 1
        
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()