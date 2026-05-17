class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        num_fleets = 0

        lsts = sorted(zip(position,speed), reverse = True)

        pos,spd = zip(*lsts)

        print(pos)
        print(spd)

        times = []
        for i in range(len(pos)):
            times.append((target-pos[i]) / spd[i])

        x = times[0]
        ct = 1

        for i in times:
            if i <= x:
                pass
            else:
                x = i
                ct += 1
        return ct
            

