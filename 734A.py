import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(n,s):
    dic = {'A':0,"D":0}
    for i in s:
        dic[i] = 1 + dic.get(i,0)
    if dic["A"] > dic["D"]:
        print("Anton")
    elif dic["D"] > dic["A"]:
        print("Danik")
    else:
        print("Friendship")

def main():   
    n = int(input())
    s = input()
    solve(n,s)

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()