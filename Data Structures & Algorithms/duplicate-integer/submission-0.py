from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        if any(v>1 for v in count.values()):
            return True
        else:
            return False
        