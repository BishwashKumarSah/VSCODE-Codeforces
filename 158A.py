import sys 
from os import path

def input():
    return sys.stdin.readline().strip()

def main():
    n,k = map(int,input().split())
    array = list(map(int, input().split()))
    kth = array[k-1]
    array.sort()
    count = -1
    for i in range(len(array)):
        if array[i] > 0 and array[i] >= kth:
            count = i
            break
    if count == -1:
        print(0)
    else:
        print(len(array[count:]))
    
if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()