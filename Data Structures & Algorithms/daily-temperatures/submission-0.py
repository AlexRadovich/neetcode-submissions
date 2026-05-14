class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        end = [0] * len(temperatures)

        for i in range(len(temperatures)):
            print(end)
            print(stack)
            print()
            item = temperatures[i]

            if not stack or item <= temperatures[stack[-1]]:
                stack.append(i)

            else:
                while stack and item > temperatures[stack[-1]]:
                    ix = stack.pop()
                    end[ix] = i - ix
                stack.append(i)

        return end

