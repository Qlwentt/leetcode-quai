class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            # same parity, found violating index
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            found_violating_index = self.binarySearch(
                start + 1, end, violating_indices
            )

            if found_violating_index:
                ans[i] = False
            else:
                ans[i] = True

        return ans

    def binarySearch(
        self, start: int, end: int, violating_indices: List[int]
    ) -> bool:
        left = 0
        right = len(violating_indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            violating_index = violating_indices[mid]

            if violating_index < start:
                # check right half
                left = mid + 1
            elif violating_index > end:
                # check left half
                right = mid - 1
            else:
                # violatingIndex falls in between start and end
                return True

        return False