import sys 
from os import path

def input():
    return sys.stdin.readline().strip()
 
def solve(k):
    ans = 0
    
    ans += k[0]
    if k[1] % 3 == 0:
        ans += (k[1] // 3)
        
        if k[2] % 3 > 0:
            ans += (k[2] // 3 ) + 1
        else:
            ans += (k[2] // 3 )
        print(ans)
        return
    else:
        if  ((k[1]% 3) + k[2])  < 3 :
            print(-1)
            return
        ans += k[1] // 3
        k[2] += k[1] % 3
        if k[2] % 3 > 0:
            ans += (k[2] // 3 ) + 1
        else:
            ans += (k[2] // 3 )
        print(ans)
        return

def main():
    t = int(input())  
    while t > 0:
        
        k = list(map(int,input().split()))
        solve(k)
        t -= 1
    

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()