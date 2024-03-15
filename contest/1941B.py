import sys 
from os import path

def input():
    # return sys.stdin.readline().strip()
    return sys.stdin.readline().strip()

def solve(n,arr):
    for i in range(1,len(arr)-1):
        if  arr[i] >= arr[i-1] *2 and arr[i+1] >= arr[i-1]:
            arr[i] -= 2 * arr[i-1]
            arr[i+1] -= arr[i-1]
            arr[i-1] = 0
    for i in arr:
        if i != 0:
            print("NO")
            return   
    print("YES")    
    const employeesData = [

{
    id:1,
    firstName:'Rohan',
    lastName:''
}
    ]      
        
        
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        a = int(input())
        arr= list(map(int,input().split()))
        solve(n,arr)
        t -= 1

if __name__  == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
        