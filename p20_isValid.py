
class Solution(object):
    def isValid(self, s:str) -> bool:
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
        


sol = Solution()
s = "()"
ouput = sol.isValid(s)
print(ouput)

# Let's walk through how the code for `isValid()` evolves based on each key question.

# 1. "What is the function supposed to return?"
# We start with just a function returning a boolean — a skeleton.
'''
step_1 = 
'''
def isValid(s: str) -> bool:
    return True  # placeholder
'''

# 2. "What defines a 'valid' string of brackets?"
# Realize we must validate matching brackets, so we need to iterate through the input.

step_2 = '''
def isValid(s: str) -> bool:
    for char in s:
        pass  # We'll process each character
    return True  # still a placeholder
'''

# 3–5. "What are possible characters? What structure helps?" → Stack idea emerges

step_3 = '''
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
    return True
'''

# 6. "What about closing brackets? How do I check matches?" → Begin to compare

step_4 = '''
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            stack.pop()
    return True
'''

# 7. "But how do I know the popped item actually matches the closing?" → Use bracket_map

step_5 = '''
def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map.values():  # opening
            stack.append(char)
        elif char in bracket_map:  # closing
            if not stack or bracket_map[char] != stack.pop():
                return False
    return True
'''

# 8. "What if there's an unmatched opening at the end?" → Final return checks empty stack

step_6 = '''
def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or bracket_map[char] != stack.pop():
                return False
    return not stack
'''

# 9. "Can I simplify the structure and avoid nested ifs?" → Tidy final version

final_step = '''
def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else '#'
            if bracket_map[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
'''
'''