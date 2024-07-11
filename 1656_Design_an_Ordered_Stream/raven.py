class OrderedStream:
  def __init__(self, n: int):
    self.q = [None] * (n + 1)
    self.p = 1

  def insert(self, idKey: int, value: str) -> List[str]:
    ret = []
    self.q[idKey] = value
    while self.p < len(self.q) and self.q[self.p] is not None:
      ret.append(self.q[self.p])
      self.p += 1

    return ret
