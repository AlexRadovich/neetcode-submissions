from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(0,len(tokens)):
            print(stack)
            
            item = tokens[i]

            if item in {"+","-","*","/"}:
                a = stack.pop()
                b = stack.pop()
                match item:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(b-a)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        k = b/a
                        if k < 0:
                            k = ceil(k)
                        else:
                            k = k//1
                        stack.append(k)
            else:
                stack.append(int(item))
        return int(stack[0])

