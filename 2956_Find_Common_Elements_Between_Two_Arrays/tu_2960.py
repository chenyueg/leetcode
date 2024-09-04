class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        for i in range(1, len(batteryPercentages)):
            test = i - batteryPercentages[:i].count(0)
            batteryPercentages[i] = max(0, batteryPercentages[i] - test)
        return len(batteryPercentages) - batteryPercentages.count(0)
        