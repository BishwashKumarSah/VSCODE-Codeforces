import sys
from os import path

def input():
    return  sys.stdin.readline().rstrip("\r\n")

def bs(low,high,res,target):
    
    while high - low > 1:
        mid = low + (high - low)//2
        if res[mid] < target:
            low = mid + 1
        else:
            high = mid
    if res[low] >= target:
        return res[low]
    return res[high]
    

def solve(lst,res,s,matrix):   
    
    ans = float("inf")
    #For Row Matrix
    for r in range(len(matrix)):
        cnt = 0
        for c in range(len(matrix[0])):
            val = bs(0,len(res)-1,res,matrix[r][c])
            cnt += val - matrix[r][c]
        ans = min(ans,cnt)
        
        
    ansC = float("inf")
    #For Row Matrix
    for c in range(len(matrix[0])):
        cnt = 0
        for r in range(len(matrix)):            
            val = bs(0,len(res)-1,res,matrix[r][c])
            cnt += val - matrix[r][c]
        ansC = min(ansC,cnt)        
    print(min(ans,ansC))

def main():   
    lst = [1] * 1000000
    for i in range(2,len(lst)):
        if lst[i] == 1:
            for j in range(i*i,len(lst),i):                
                if lst[j] >1:
                    continue
                lst[j] += 1
    res = []
    for i in range(2,len(lst)):
        if lst[i] == 1:
            res.append(i)
    s = set(res)    
    r,c = map(int,input().split())
    matrix = [list(map(int,input().split())) for i in range(r)]
    
            
    solve(lst,res,s,matrix)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()