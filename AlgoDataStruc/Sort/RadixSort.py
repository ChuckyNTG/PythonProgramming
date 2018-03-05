
nums = map(int, raw_input().split(' '))

buckets = [] * 10

#Split into buckets
i = 1
while i< max(nums):
   divisior = max(nums)/i
