
# 416. Partition Equal Subset Sum


class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()

            for t in dp:
                if (t + nums[i]) == target:
                    return True

                nextDP.add(t + nums[i])
                nextDP.add(t)

            dp = nextDP

        return True if target in dp else False


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    objectNums = Solution()
    print(objectNums.canPartition(nums))
