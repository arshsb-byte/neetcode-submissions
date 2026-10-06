class Solution:
    @staticmethod
    def comp(s:str)-> str:
        if s == "(":
            return ")"
        elif s == "[":
            return "]"
        elif s == "{":
            return "}"

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if (len(stack)>0 and s[i] == self.comp(stack[-1])):
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack)==0
        