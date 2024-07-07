class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        allkeys = [c for c in key if c.islower()]
        keys = []
        while len(keys) < 26:
            current = allkeys.pop(0)
            if current not in keys:
                keys.append(current)
        lowers = list(map(chr, range(97, 123)))
        assert(len(lowers) == len(keys))
        mydict = str.maketrans(''.join(keys), ''.join(lowers))
        return message.translate(mydict)