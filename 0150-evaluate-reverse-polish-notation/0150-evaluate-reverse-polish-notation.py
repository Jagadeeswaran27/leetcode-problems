class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            # print("Current Stack",stack)
            # print("Symbol",c)
            if c == "+":
                # print("Plus operation")
                a,b = stack.pop(),stack.pop()
                stack.append(a+b)
            elif c == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == "*":
                a,b = stack.pop(),stack.pop()
                stack.append(a*b)
            elif c == "/":
                a,b = stack.pop(),stack.pop()
                # print("Stack data ",a,b)
                # print("Updated Stack 1 ",stack)
                stack.append(int(b/a))
                # print("Updated Stack 2 ",stack)
            else:
                stack.append(int(c))
        
        return stack[-1]