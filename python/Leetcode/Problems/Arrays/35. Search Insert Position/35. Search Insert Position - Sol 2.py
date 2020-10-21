class Solution:

    def main(self):

        a = [1, 3, 5, 6, 9, 10]
        target = 7

        output = self.searchInsert(a, target)
        print('output =', output)

    def searchInsert(self, nums, target):

        if (len(nums) > 10 ** 4) or len(nums) < 1:
            return -1
        if (target > 10 ** 4) or target < -10 ** 4:
            return -1

        r = len(nums) - 1
        l = 0
        mid = 0

        while l <= r:
            mid = int(l + ((r - l) / 2))
            # print('mid =', mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
        return l


s = Solution()
s.main()
