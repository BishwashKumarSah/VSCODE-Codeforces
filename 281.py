import sys
from os import path

def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    print(s[0].title() + s[1:])
    
if __name__ == "__main__":
    if(path.exists("input.txt")):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()