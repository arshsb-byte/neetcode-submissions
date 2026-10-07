class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if (tokens[i] in ["+","-","*","/"]):
                    b = int(stack[-1])
                    a = int(stack[-2])
                    stack.pop()
                    stack.pop()
                    if(tokens[i] == "+"):
                        stack.append(a+b)
                    elif(tokens[i] == "-"):
                        stack.append(a-b)
                    elif(tokens[i] == "*"):
                        stack.append(a*b)
                    elif(tokens[i] == "/"):
                        stack.append(int(a/b))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]
        