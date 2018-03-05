class Solution(object):
    def letterCombinations(self,digits):
        import itertools
        pad = [None,None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if not digits.isdigit():
            return []
        letters = ''
        c = pad[int(digits[0])]
        for i in range(1,len(digits)):
            combo = list(itertools.product(c,pad[int(digits[i])]))
            c = [c[0] + c[1] for c in combo]
        return c

s = Solution()
print s.letterCombinations('234')
       
