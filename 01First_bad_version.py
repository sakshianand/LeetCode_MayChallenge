# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n

        while (s < e):
            mid = int(s + (e - s) / 2)
            if (isBadVersion(mid)):
                e = mid
            else:
                s = mid + 1
        return s
