import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(y):
    st = str(y)
    while True:
        st = str(int(st)+1)
        if st[0] != st[1] and st[0] != st[2] and st[0] != st[3] and st[1] != st[2] and st[1]!= st[3] and st[2] != st[3]:
            print(st)           
            break

def main():   
    y = int(input())
    solve(y)

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()