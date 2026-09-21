class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sor = sorted(nums)
        num_set = set(sor)
        longest = 0

        if not nums:
            return 0

        for n in num_set:
            if n -1 not in num_set:
                current_num = n 
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest,current_length)
        
        return longest
