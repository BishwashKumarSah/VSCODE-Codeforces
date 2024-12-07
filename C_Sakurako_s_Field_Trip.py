import sys
from os import path

def input():
    return sys.stdin.readline().strip()

def solve(n, lst):  
    # Recursive function to find the minimum number of adjacent identical elements
    cache = {}
    def recu(i):
        # Base case: If we've processed the first half of the list
        if i >= n // 2:
            # Count adjacent identical elements
            c = 0
            for x in range(len(lst) - 1):
                if lst[x] == lst[x + 1]:
                    c += 1
            return c
        if i in cache:
            return cache[i]
        
        # Don't swap the current index and calculate result
        res = recu(i + 1)
        
        # Swap the current index with its counterpart and calculate result
        j = n - i - 1  # Correct counterpart index
        lst[i], lst[j] = lst[j], lst[i]
        res = min(res, recu(i + 1))
        # Undo the swap (backtracking step)
        lst[i], lst[j] = lst[j], lst[i]
        cache[i] = res
        return cache[i]
    
    # Start recursion from index 0
    print(recu(0))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        solve(n, lst)

if __name__ == "__main__":
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()
