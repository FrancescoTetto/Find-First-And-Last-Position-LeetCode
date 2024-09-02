class Solution(object):
    def searchRange(self, nums, target):
        not_found = [-1, -1]
        found = []
        if target not in nums:
            return not_found

        for index, value in enumerate(nums):
            if value == target:
               found.append(index)

        if len(found) == 1:
              found.append(nums.index(target))
        
        if len(found) > 2:
            return [found[0], found[-1]]
        return found

solution = Solution()
nums = [3, 3, 3]
target = 3
print(solution.searchRange(nums, target))


