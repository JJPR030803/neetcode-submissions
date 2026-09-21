class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        freq = {}
        max_window = 0

        while right < len(s):

            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            max_freq = max(freq,key=freq.get)
            while (right - left +1) - freq[max_freq] > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                if freq:
                    max_freq = max(freq,key=freq.get)
                left += 1


            max_window = max(max_window,(right-left+1))
            right += 1
        
        return max_window