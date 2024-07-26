import sys
from os import path
import math
from collections import *
from copy import deepcopy

def input():
    return sys.stdin.readline().strip()


def solve(n,q,s1,s2,query):
    lst = []
    dic = defaultdict(int)
    for i in s1:
        dic[i] += 1
        lst.append(deepcopy(dic))
    lst1 = []
    dic1 = defaultdict(int)
    for i in s2:
        dic1[i] += 1
        lst1.append(deepcopy(dic1))
   
    results = []
    for first, last in query:
        l = first - 1
        r = last - 1
        
        if l > 0:
            freq_s1_left = lst[l - 1]
            freq_s2_left = lst1[l - 1]
        else:
            freq_s1_left = defaultdict(int)
            freq_s2_left = defaultdict(int)
        
        freq_s1_right = lst[r]
        freq_s2_right = lst1[r]
        
        mismatch_count = 0
        for char in set(freq_s1_right.keys()).union(set(freq_s2_right.keys())):
            freq_s1 = freq_s1_right[char] - freq_s1_left.get(char, 0)
            freq_s2 = freq_s2_right[char] - freq_s2_left.get(char, 0)
            mismatch_count += abs(freq_s1 - freq_s2)
        
        results.append(mismatch_count // 2)
    
    for result in results:
        print(result)
    
    
    

def main():
    t = int(input())
    for _ in range(t):
        n,q = list(map(int,input().split()))
        s1 = input()
        s2 = input()
        lst = []
        for _ in range(q):
            val = list(map(int,input().split()))
            lst.append(val)
        
        
        solve(n,q,s1,s2,lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()