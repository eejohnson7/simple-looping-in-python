'''
In this task, you are to write a Python function that implements the concept of Run-Length Encoding (RLE) on an alphanumeric 
input string. Run-length encoding is a simple form of data compression where sequences of data entities that are the same are 
stored as a single data entity along with its count. Each count must immediately follow the character it is associated with.

Your function's name should be encode_rle. It takes a string as an input argument and returns a new string that represents the 
input's run-length encoding.


Your function should operate only on alphanumeric characters (numbers 0-9 and uppercase and lowercase letters A-Z, a-z). 
For any other types of characters in the string, simply ignore them and do not include them in the final encoded output.

For instance, if the input string is "aaabbcccdde", the output should be "a3b2c3d2e1". If the input string includes 
non-alphanumeric characters, such as "aaa@@bb!!c#d**e", the output should be "a3b2c1d1e1".

We assume that the given input string could have up to 500 characters.

Good luck! We believe you can successfully manage this task!
'''

def encode_rle(s):
    # TODO: implement
    current_char = None
    current_length = 0
    result = ""
    
    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_char:
                current_length += 1
            else:
                if current_char is not None:
                    result = result + current_char + str(current_length)
                current_char = char
                current_length = 1
                
    if current_char is not None:
        result = result + current_char + str(current_length)
                
    return result