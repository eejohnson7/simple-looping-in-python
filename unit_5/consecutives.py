'''
Your task is to write a Python function that takes in a string and identifies all the consecutive groups of identical 
characters within it, with the analysis starting from the end of the string rather than from its beginning. A group is 
defined as a segment of the text where the same character is repeated consecutively.

Your function should return a list of tuples. Each tuple will consist of the repeating character and the number of its 
repetitions. For instance, if the input string is "aaabbcccdde", the function should output: [('e', 1), ('d', 2), ('c', 3), 
('b', 2), ('a', 3)].

Note that the input string cannot be empty; in other words, it must contain at least one character, and its length must not 
exceed 500 characters. The return should also be in reverse order, starting from the group of repeated characters at the end 
of the string and moving backward.

Put your knowledge and skills into action to solve this reverse pattern identification puzzle!
'''

def solution(s):
    # TODO: implement the algorithm to find consecutive groups of characters in the reverse order
    previous_char = None
    count = 0
    result = []
    length = len(s)
    
    for i in range(length):
        char = s[length - i - 1]
        
        if char == previous_char:
            count += 1
        else:
            if previous_char is not None:
                result.append((previous_char, count))
            previous_char = char
            count = 1
            
    if previous_char is not None:
        result.append((previous_char, count))
    
    return result