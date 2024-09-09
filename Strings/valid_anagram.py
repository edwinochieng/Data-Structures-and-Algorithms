#Solution One (Using Hashmaps)

def validAnagram(s,t):

    if len(s) != len(t):
        return False
  
    count = {}

    for char in s:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -=1
    
    return True



#Solution Two (Sorting) 

def isAnagram(s,t):

    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)
    





