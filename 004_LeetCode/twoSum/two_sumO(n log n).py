class Solution:
    def twoSum(nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:

            golden_ticket = nums[left_pointer] + nums[right_pointer]

            if golden_ticket == target:
                return [left_pointer, right_pointer]

            elif golden_ticket < target:
                left_pointer += 1

            elif golden_ticket > target:
                right_pointer -= 1

        return []


nums = [3,2,4]
target = 6

print(Solution.twoSum(nums, target))
