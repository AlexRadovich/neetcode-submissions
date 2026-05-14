class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0) + 1
        lst = []
        for _ in range(len(dic.keys())+1):
            lst.append([])
        for i in dic.keys():
            lst[dic[i] * len(dic.keys()) // max(dic.values()) ].append(i)
        g = []
        ct = 0
        ix = -1
        print(lst)
        while(ct<k):
            if len(lst[ix]) != 0:
                for i in lst[ix]:
                    g.append(i)
                ct += len(lst[ix])
            ix -=1 
        print(g)
        return g