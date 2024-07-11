class Solution:
  def validStrings(self, n: int) -> List[str]:
    if n == 1:
      return ['0', '1']
    pre = self.validStrings(n - 1)
    
    ret = []
    for i in pre:
      last = i[-1] 
      if last == '0':
        ret.append(i + '1')
      else:  
        ret.append(i + '0')
        ret.append(i + '1')
    
    return ret
        
