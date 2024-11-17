from typing import List

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        modV = 10**9 + 7
        memo = {}

        def recu(ind, last_value):
            if ind == len(nums):
                return 0

            # If we have already computed this state, return it
            if (ind, last_value) in memo:
                return memo[(ind, last_value)]

            # Option 1: Skip current number
            skip = recu(ind + 1, last_value)

            # Option 2: Include current number (if it satisfies the abs difference condition)
            include = 0
            if last_value == -1 or abs(last_value - nums[ind]) == 1:
                include = (nums[ind] + recu(ind + 1, nums[ind])) % modV

            # Total is the sum of both options
            result = (skip + include) % modV

            # Save the computed result for this state
            memo[(ind, last_value)] = result
            return result

        # Start recursion from index 0 with an invalid last_value (-1)
        return recu(0, -1)
