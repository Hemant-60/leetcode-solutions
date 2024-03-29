class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(patt, word):
            occ=[None for i in range(26)]
            for i in range(len(word)):
                if occ[ord(patt[i])-ord('a')]==None:
                    occ[ord(patt[i])-ord('a')] = word[i]
                else:
                    if occ[ord(patt[i])-ord('a')] !=word[i]:
                        return False
            return True
        res=[]
        for word in words:
            if encode(pattern, word) and encode(word, pattern):
                res.append(word)
        return res
