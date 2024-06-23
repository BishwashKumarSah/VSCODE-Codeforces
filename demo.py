i = 0
        j = 1
        ans = 0
        val = nums[0]
        s = set()
        s.add(nums[0])

        while j < len(nums):
            if j % 2 == 0 and nums[j] >= 0 and nums[j] not in s:
                val += nums[j]
                s.add(nums[j])
                j += 1
            elif j % 2 != 0 and nums[j] < 0 and nums[j] not in s:
                val += nums[j] * (-1)
                
                s.add(nums[j])
                j += 1
            else:
                i = j
                ans += val
                val = nums[i]
                s.clear()
                s.add(nums[i])
                j += 1

        return ans + val