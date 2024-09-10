def canConstruct(ransomNote,magazine):

    counter = {}

    for char in magazine:
        if char in counter:
            counter[char] +=1
        else:
            counter[char] = 1

    
    for char in ransomNote:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True
