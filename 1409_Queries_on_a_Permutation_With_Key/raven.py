class Solution:
  def processQueries(self, queries: List[int], m: int) -> List[int]:
    p = [i for i in range(1, m + 1)]

    ret = []
    for q in queries:
      idx = p.index(q)
      ret.append(idx)
      v = p.pop(idx)
      p.insert(0, v)
      
    return ret
   
