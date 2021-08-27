from  math import log,ceil,floor
class Solution:
    
    def poorPigs(self, b: int, md: int, mt: int) -> int:
        return ceil(log(b)/log(ceil(mt/md+1)))
