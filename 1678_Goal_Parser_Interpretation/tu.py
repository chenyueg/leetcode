class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        sign_o = 0
        sign_al = 0
        for i in range(len(command)):
            if command[i] == "G":
                    result += "G"
            elif command[i] == "(":
                    sign_o = 1
                    sign_al = 1
            elif command[i] == ")":
                if sign_o == 1:
                    result += "o"
                    sign_o = 0
                    sign_al = 0
                    continue
                if sign_al == 3:
                    result += "al"
                    sign_o = 0
                    sign_al = 0
                    continue
            elif command[i] == "a" or command[i] == "l":
                if sign_al > 0:
                    sign_al += 1
                    sign_o = 0
                    continue
        return result


