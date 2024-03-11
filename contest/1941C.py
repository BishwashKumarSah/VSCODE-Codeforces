import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n,s):
    ans = 0
    if "mapie" in s:
        ans += s.count("mapie")
        s = s.replace("mapie","maie") 
    ans += s.count("pie") + s.count("map")
    print(ans)

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        s = input()
        
        solve(n,s)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        