class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        if len(tasks) == 1:
            return sum(tasks[0])
        
        min_task = sum(tasks[0])
        for i in range(1, len(tasks)):
            min_task = min(min_task, sum(tasks[i]))
        return min_task