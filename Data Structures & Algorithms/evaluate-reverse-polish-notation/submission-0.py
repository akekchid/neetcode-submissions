class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        stack = []

        for i in tokens:
            if i in ops:
                operand2 = stack.pop()
                operand1 = stack.pop()

                answer = ops[i](operand1, operand2)
                stack.append(answer)
            else:
                stack.append(int(i))

        return stack[0]
        