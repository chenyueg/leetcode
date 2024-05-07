class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        max_num = max(num_dict, key=num_dict.get)
        max_count = num_dict[max_num]

        result = []
        for i in range(max_count):
            result.append([])

        for num in num_dict:
            for i in range(num_dict[num]):
                result[i].append(num)

        return result