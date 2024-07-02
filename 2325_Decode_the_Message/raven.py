class Solution:
  def decodeMessage(self, key: str, message: str) -> str:
    dic = {' ': ' '}
    char = 97
    for k in key:
      if k.isalpha() and char < 97 + 26 and k not in dic:
        dic[k] = chr(char)
        char += 1
    
    return ''.join([dic[i] for i in message]) 
