class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if(i=="*" or i=="+" or i=="-" or i=="/"):
                if(i=="*"):
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
                elif(i=="+"):
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
                elif(i=="-"):
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
                else:
                    if(stack[-1] and stack[-2] and i=="/"):
                        a=stack.pop()
                        b=stack.pop()
                        # print(int(b/a))
                        stack.append(int(b/a))
                    else:
                        stack.pop()
                        stack.pop()
                        stack.append(0)
            else:
                stack.append(int(i)) 
                # print(stack)
        return(stack[-1])

        