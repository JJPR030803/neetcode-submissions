class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        w = ""
        for word in strs:
            w = sorted(word)
            h.setdefault(''.join(w),[]).append(word)
        
        return list(h.values())
