class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_types = ['G', 'P', 'M']
        gar_dict = {}
        result = 0
        for gar_type in garbage_types:
            gar_dict[gar_type] = {}
            largest = 0
            for i in range(len(garbage)):
                g = garbage[i]
                count = g.count(gar_type)
                if count:
                    gar_dict[gar_type][i] = count
                    largest = i
            # calculate route cost
            if largest > 0:
                result += sum(travel[:largest])
            # calculate collect cost
            result += sum(gar_dict[gar_type].values())
        return result
