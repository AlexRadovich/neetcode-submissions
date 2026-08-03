class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])

        print(diff)

        if sum(diff) < 0:
            return -1

        total = 0
        res = 0

        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                res = i + 1

        return res
