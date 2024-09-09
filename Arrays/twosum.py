def twoSum(arr,target):
    numMap = {} # value:index
    
    for i,n in enumerate(arr):
        diff = target - n
        
        if diff in numMap:
            return [numMap[diff], i]
        else:
            numMap[n] = i
            
    return []

            