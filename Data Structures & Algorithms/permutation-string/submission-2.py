class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = len(s1)-1

        left = 0

        s1_freq = {}
        s2_freq = {}

        for st in s1:
            if st in s1_freq:
                s1_freq[st]+=1
            else:
                s1_freq[st]=1
        
        for st in s2[left:right+1]:
            if st in s2_freq:
                s2_freq[st]+= 1
            else:
                s2_freq[st] = 1

        if s1_freq == s2_freq:
            return True
        while left < right < len(s2)-1:

           

            s2_freq[s2[left]]-=1

            if s2_freq[s2[left]] == 0:
                del s2_freq[s2[left]]

            left += 1
            right += 1

            if s2[right] in s2_freq:
                s2_freq[s2[right]]+=1
            else: 
                s2_freq[s2[right]] = 1

            if s1_freq == s2_freq:
                return True

        return False