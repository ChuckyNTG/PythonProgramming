
def subsets(nums):

    def combos(nums):
        if len(nums) == 1:
            return [nums]

        res = []
        res.append([nums[0]])
    
        for r in combos(nums[1:]):
            res.append(r)
            res.append([nums[0]] + r)

        return res


    res = combos(nums)
    res.insert(0,[])
    return res

print subsets([1,2,3,4])
