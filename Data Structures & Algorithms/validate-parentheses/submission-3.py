class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {   ')': '(',   ']': '[',    '}': '{'}
        for c in s:
            if c in matching_brackets:
                if not stack:
                    return False
                cur = stack.pop()
                if cur != matching_brackets[c]:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
