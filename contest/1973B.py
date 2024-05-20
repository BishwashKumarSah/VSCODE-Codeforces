        ns = [str(num) for num in nums]        
        leng = len(ns[0])        
        diff = 0
        n = len(nums)       
        
        for pos in range(leng):
            dig_con = [0] * 10
            for num in ns:
                dig_con[int(num[pos])] += 1            
            for i in range(10):
                for j in range(10):
                    if i != j:
                        diff += dig_con[i] * dig_con[j]        
        return diff // 2