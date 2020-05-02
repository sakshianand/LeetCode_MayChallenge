class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        mySet = set(J)
        count = 0
        for c in S:
            if c in mySet:
                count += 1
        return count
