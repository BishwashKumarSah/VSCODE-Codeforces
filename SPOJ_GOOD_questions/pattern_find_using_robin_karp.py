import sys
import collections

from os import path


def input():
    return  sys.stdin.readline().rstrip("\r\n")
prime = 27
MOD = 1000000007 
MAX_VAL = int(1e6+7)
power = [0] * MAX_VAL
power[0] = 1
def Compute():      
    global power
    for i in range(1,len(power)):
        power[i] = (power[i-1] * prime)%MOD

def solve(s1,s2):
    
    #Calculating Pattern Hash Value    
    req = 0
    for i in range(0,len(s2)):
        val = (ord(s2[i]) - ord('a') )+ 1
        val = (val * power[i]) % MOD
        req += val

    
    #Prefix Sum Array.     
    arr = [0] * len(s1)    
    arr[0] = ((ord(s1[0]) - ord('a')) + 1 ) 
    for i in range(1,len(s1)):
        v = (((ord(s1[i]) - ord('a'))+1) * power[i]) % MOD 
        arr[i] = arr[i-1] + v
        
    i = 0
    j = len(s2) - 1
    res = []
    c = 0
    while j < len(s1):
    
        if i == 0:
            if arr[j] == req:
                c += 1
                res.append(i+1)
        else:
            diff = (arr[j] - arr[i-1] + MOD) % MOD
            r = (req * power[i])%MOD
            if diff == r:
                res.append(i+1)
                c += 1
        
        i += 1
        j += 1
    
    if c == 0:
        print("Not Found") 
        return    
    print(end="\n")         
    print(c)
    print(*res)
    print(end="\n")   

   
def main():  
    Compute()      
    t = int(input()) 
    for _ in range(t):
        s1,s2 = map(str,input().split())
        solve(s1,s2)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()