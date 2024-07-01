class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alp = "abcdefghijklmnopqrstuvwxyz"
        decoder = {}
        answer = ""
        index = 0
        
        for char in key:
            if char != " " and char not in decoder:
                decoder[char] = index
                index += 1
        
        for char in message:
            if char == " ":
                answer += " "
            else:
                answer += alp[decoder[char]]

        return answer