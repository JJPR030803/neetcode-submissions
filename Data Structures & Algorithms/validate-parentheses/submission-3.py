class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_set = {'}':'{',']':'[',')':'('}

        for c in s:
            if c not in hash_set:
                stack.append(c)
            else:
                if stack:
                    value = stack.pop()
                    if hash_set[c] != value:
                        return False
                        break
                else:
                    return False
        return len(stack) <= 0