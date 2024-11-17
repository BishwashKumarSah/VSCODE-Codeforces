
        dic = collections.Counter(word2)
        countT = len(dic)
        
        
        dicS = {}
        i, j = 0, 0
        countS = 0
        valid_count = 0
        
        while j < len(word1):
           
            char = word1[j]
            if char in dic:
                dicS[char] = dicS.get(char, 0) + 1
                if dicS[char] == dic[char]:
                    countS += 1
            
         
            while countS == countT:
              
                valid_count += len(word1) - j
                
              
                left_char = word1[i]
                if left_char in dicS:
                    dicS[left_char] -= 1
                    if dicS[left_char] < dic[left_char]:
                        countS -= 1
                    if dicS[left_char] == 0:
                        del dicS[left_char]
                
                i += 1
            
         
            j += 1
        
        return valid_count