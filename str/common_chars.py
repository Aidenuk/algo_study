#leetcode 1002


# def commonChars(words):
#     common_chars = []
#     common_chars.append(list(words)[0])
#     result = []
#     for i in range(len(words)):
#         for each_char in words[i]:
#             newlist = list(common_chars[0])
#             if each_char in newlist:
#                 result.append(each_char)

#     print(result)
    




def commonChars(words):
    if not words:
        return []
    
    common_chars = list(words[0])
    result = []
    for char in common_chars:
        appears_in_all = True
        for word in words:
            if char not in word:
                appears_in_all = False
                break
        if appears_in_all:
            result.append(char)
            for i in range(len(words)):
                words[i] = words[i].replace(char, '', 1)
            print(words)
    
    return result

print(commonChars(['cool', 'lock', 'cook']))
