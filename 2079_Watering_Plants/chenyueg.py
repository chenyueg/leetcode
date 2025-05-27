class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n=-1 
        steps = 0
        cap = capacity

        while n < len(plants)-1:
            if cap >= plants[n+1]:
                steps += 1
                cap -= plants[n+1]
                n += 1
            else:
                steps += (2*n + 3)
                cap = capacity 
                cap -= plants[n+1]
                n += 1

        return steps