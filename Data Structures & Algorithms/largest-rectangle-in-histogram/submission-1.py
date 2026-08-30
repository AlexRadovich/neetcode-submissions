class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(-1)

        stack = []
        best = 0

        for ix, val in enumerate(heights):
            #print('STACK', stack)
            if not stack or stack[-1][1] <= val:
                stack.append((ix,val))
                #print('v1')
            else:
                while stack and val < stack[-1][1]:
                    ht = stack[-1][1]
                    top = stack.pop()[0]
                    # print('STACK', stack)
                    # print('top',top)
                    # print((ix-top) * heights[top], "HERE", top, ix)
                    best = max(best, (ix-top) * ht)
                stack.append((top,val))
                #print('v2')

        return best

            