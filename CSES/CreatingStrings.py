import sys
import collections

from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def solve(dic,res,ans,n):
    if len(ans) == n:
        res[0] += 1
        res.append(ans[:])
        return
    for i in dic:
        if dic[i] > 0:
            dic[i] -= 1
            ans += i
            solve(dic,res,ans,n)
            ans = ans[:-1]
            dic[i] += 1

def main():        
    res = [0]
    s = input()
    s = list(s)
    s.sort()
    s = "".join(s)    
    n = len(s)
    dic = collections.Counter(s)
    solve(dic,res,"",n)
    print(res[0])
    
    for r in range(1,len(res)):
        print(res[r],end="\n")

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()