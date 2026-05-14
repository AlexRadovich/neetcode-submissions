class Solution:
    def trap(self, height: List[int]) -> int:
        aux_left = [0] * len(height)
        aux_right = [0] * len(height)
        for i in range(len(height)):
            r_ix = len(height)-1-i
            if(i==0):
                aux_left[0] = height[0]
                aux_right[-1] = height[-1]
                continue
            aux_left[i] = max(aux_left[i-1],height[i])
            aux_right[r_ix] = max(aux_right[r_ix+1], height[r_ix])

        ret = 0
        for i in range(len(height)):
            ret += min(aux_left[i],aux_right[i])-height[i]
        print(aux_left)
        print(aux_right)

        return ret
