import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap, max_heap = [], []
        n = len(nums)
        left = 0
        answer = 0
        for right in range(n):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            while min_heap[0][1] < left:
                heapq.heappop(min_heap)
            while max_heap[0][1] < left:
                heapq.heappop(max_heap)

            if -max_heap[0][0] - min_heap[0][0] <= limit:
                answer = max(answer, right - left + 1)
            else:
                left += 1
        return answer