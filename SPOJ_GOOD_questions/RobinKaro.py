import sys
from os import path
import math
from collections import *

def input():
    return sys.stdin.readline().strip()

prime = 27
MOD = 1000000007 
MAX_VAL = int(1e6+7)
power = [0] * MAX_VAL
power[0] = 1
def Compute():      
    global power
    for i in range(1,len(power)):
        power[i] = (power[i-1] * prime)%MOD
def solve( s1, s2):
        # we are taking prime 31 because we need some values greater than 26 since total a-z is 26. 
        #also in this question All character will be lower case Latin character.
        # but if there is both A-Za-z then 26+26 = 42 take prime greater than 42 ie 47
        #if we take prime = 5 which is less than 26 then for
        #eg f => (('f'-'a'+1)* (5)^0 => 6) 'aa' => (('a'-'a'+1) * (5)^0 +('a'-'a'+1) * (5)^1) = 6
        #here both of them have same value so it will not give unique value same for +1 
        # 'a' and 'aa' if we dont add 'a'-'a' (+ 1) here it will give 0 and for 'aa' it will also be 0.
        # so to get uniques values we do +1. cuz the prime will give a unique value.
    # prime = 31
    # mod = 1000000007 #cuz our value may cause overflow if we keep mulitply the power so using mod.
    S = len(s1)
    P = len(s2)
    
    #first calculate the power array because everytime we DONOT want to again calculate the power as it will be costly for large input
    # for lets say i = 10^5 i want the power i donot want to get all the power and muliply it again.
   
    # power = [1] * max(S,P)
    # for i in range(1,len(power)):
    #     # here every time the power is increasing like 
    #     # power = [1, p, p*p, p*p*p, p*p*p]
    #     power[i] = (power[i-1] * prime) % mod
        
    patternHash = ord(s2[0]) - ord('a') + 1
    # calculate the hash value for the pattern.
    for i in range(1,len(s2)):
        val = ((ord(s2[i]) - ord('a') + 1) * power[i]) % MOD
        patternHash += val
    
    originalString = [1] * max(S,P)
    originalStringHash = ord(s1[0]) - ord('a') + 1
    originalString[0] = originalStringHash
    for i in range(1,len(s1)):
        val = ((ord(s1[i]) - ord('a') + 1) * power[i]) % MOD
        originalString[i] = originalString[i-1] + val
        
    # print(patternHash)
    # print(originalString)
    
    #using sliding window. to get len K and match pattern hash and originalString Hash value.
    res = []
    for i in range(0,S-P+1):
        if i == 0:
            if patternHash == originalString[P-1]:
                res.append(i+1)
        else:
            # first get the prefix 
            # instead of using the division like (x*p^2 + x*p^3)/p^2 = y * p^0 + y * p^1 => here the division will take logn tc. 
            # we need to get o(1) so just multiply on right side expression.
            # x*p^2 + x*p^3 = (y * p^0 + y * p^1) * p^2
            prefixHashValue = originalString[i+P-1] - originalString[i-1]
            requiredPatternHashValue = (patternHash * power[i]) % MOD
            
            if prefixHashValue == requiredPatternHashValue:
                res.append(i+1)
    if len(res) == 0:
        print("Not Found")
        
        return
    print(len(res))
    print(*res)
    
            
        
def main():
    Compute()
    t = int(input())
    for _ in range(t):        
        s1,s2 = map(str,input().split())
        solve(s1,s2)
        print('\n')

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()