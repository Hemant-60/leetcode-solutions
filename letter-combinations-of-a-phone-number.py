class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {2:0, 3:3, 4:6, 5:9, 6:12, 7:15, 8:19, 9:22}
        
        def get_arr(a):
            return [chr(ord('a') + keys[a] + i) for i in range(4 if a==7 or a==9 else 3)]
            
        def get_comb(a, b):
            return get_arr(a) if not b else [j+i for i in get_arr(a) for j in b]
        
        res = []
        for i in digits: res = get_comb(int(i), res)
        return res
