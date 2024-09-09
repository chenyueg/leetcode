class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = date.split('-')
        res = []

        for char in date_list:
            binary = bin(int(char))
            res.append(binary[2:])
        
        return '-'.join(res)