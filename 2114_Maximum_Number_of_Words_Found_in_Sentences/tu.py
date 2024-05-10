class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        item_list = [sen.split(' ') for sen in sentences]
        return max(len(item) for item in item_list)
