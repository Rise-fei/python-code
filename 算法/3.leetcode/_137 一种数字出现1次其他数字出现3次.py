from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if mapping.get(i):
                mapping[i] += 1
            else:
                mapping[i] = 1
        for key, v in mapping.items():
            if v == 1:
                return key


s = Solution()
ret = s.singleNumber([2,2,2,1])
print(ret)
