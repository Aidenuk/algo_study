


def commonChars(words):
    common_chars = []
    common_chars.append(list(words)[0])
    result = []
    for i in range(len(words)):
        for each_char in words[i]:
            newlist = list(common_chars[0])
            if each_char in newlist:
                result.append(each_char)

    print(result)
    
        
        
        
        
    
    



print(commonChars(['cool', 'lock', 'cook']))

