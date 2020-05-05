class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        count = 1
        for ind,elem in enumerate(s):
            if elem in map:
                map[elem][0]+=1
            else:
                map[elem]=[count,ind]
        
        for ind,elem in enumerate(map):
            if map[elem][0] == 1:
                return map[elem][1]
        return -1
