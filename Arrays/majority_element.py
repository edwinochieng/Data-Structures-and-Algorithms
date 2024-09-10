# Solution One (Using a HashMap)
def majorityElement(nums):

    count = {}

    for num in nums:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1
        
        if count[num] > len(nums)//2:
            return num

# Time complexity: O(n) , Space Complexity: O(n)




## Solution Two (Boyer-Moore Voting Algorithm) - more optimal solution

def isMajority(nums):
    count = 0
    result = 0

    for num in nums:
        if count == 0:
            result = num
        if num == result:
            count +=1
        else:
            count -=1

    return result

## Time Complexity: O(n) , Space Complexity: 0(1)