class Solution:
    def reverseByType(self, s: str) -> str:
        LR = []
        SP = []

        for a in s:
            if "a" <= a <= "z":
                LR = [a] + LR
            else:
                SP = [a] + SP
        
        out = []
        lr = 0
        sp = 0

        for a in s:
            if "a" <= a <= "z":
                out.append(LR[lr])
                lr += 1
            else:
                out.append(SP[sp])
                sp += 1


        return "".join(out)