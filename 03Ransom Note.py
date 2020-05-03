class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map={}
        for elem in magazine:
            if elem in map:
                map[elem]+=1
            else:
                map[elem]=1
        
        for r in ransomNote:
            if r in map:
                if map[r]==0:
                    return False
                else:
                    map[r]-=1
            else:
                return False
            
        return True
