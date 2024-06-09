@lru_cache(None) 
    def maxTotalReward(self, lst: List[int]) -> int:
        lst.sort()
        return self.recu(0, lst, 0)
    
    def recu(self, ind: int, lst: List[int], val: int) -> int:
        if ind == len(lst):
            return val
        
        take_reward = 0
        if lst[ind] > val:
            take_reward = lst[ind] + self.recu(ind + 1, lst, val + lst[ind])
        
        skip_reward = self.recu(ind + 1, lst, val)
        
        return max(take_reward, skip_reward)