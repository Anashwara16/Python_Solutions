
# 287. Find the Duplicate Number


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    objectNums = Solution()
    print(objectNums.findDuplicate(nums))
