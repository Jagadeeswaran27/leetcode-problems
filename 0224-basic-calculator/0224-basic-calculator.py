class Solution:
    def calculate(self, x: str) -> int:

        x = x.replace(" ","")

        if x[0] == "-":
            x = "0"+x
        
        i = 0
        s = ""
        while i<len(x):
            if x[i] == "-" and x[i-1] == "(":
                s = s+"0-"
            else:
                s+=x[i]
            i+=1
        
        i=0
        res = []
        print("s",s)
        while i<len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i+=1
                print("appending...",num)
                res.append(str(num))
            else:
                print("appending...",s[i])
                res.append(s[i])
                i+=1
        
        res = self.infix_to_postfix(res)
        return self.postfix_evaluate(res)
       
    
    def postfix_evaluate(self,res):
        stack = []

        for c in res:
            if c == "+":
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
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[-1]
    
    def infix_to_postfix(self,s):
        res = []
        stack = []
        for c in s:
            if c.isalnum():
                res.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1]!="(":
                    res.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1]!="(" and (self.prec(stack[-1])>=self.prec(c) and c!="^")):
                    res.append(stack.pop())
                stack.append(c)
        
        while stack:
            res.append(stack.pop())
        
        return res
    
    def prec(self,c):
        if c == "+" or c =="-":
            return 1
        if c == "*" or c =="/":
            return 2
        if c == "^":
            return 3
        return 0