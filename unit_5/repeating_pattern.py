'''
In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function 
should identify when the same pair of characters appear next to each other in the string and count how many times each pair 
repeats consecutively.

The function should return a new string that lists each pair followed by the number of times it repeats consecutively. 
For example, let's break down the input string "aaabbabbababacab":

Divide the string into pairs:

"aa"
"ab"
"ba"
"bb"
"ab"
"ab"
"ac"
"ab"
Note the consecutive pairs:

"ab" appears twice consecutively in the middle.
Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".

Key points to remember:

The input string always has an even number of characters.
The string contains only lowercase letters.
The string length can be up to 500 characters.
Focus on finding consecutive repetitions of the same two-character patterns.
'''

def solution(s):
    # TODO: Implement the function here
    previous_pattern = None
    count = 0
    result = ""
    
    for i in range(0, len(s), 2):
        pattern = s[i:i + 2]
        
        if pattern == previous_pattern:
            count += 1
        else:
            if previous_pattern is not None:
                result = result + previous_pattern + str(count)
            previous_pattern = pattern
            count = 1
            
    if previous_pattern is not None:
        result = result + previous_pattern + str(count)
            
    return result